import dataclasses

from collections import defaultdict
from typing import Optional


class SeriesCollection:
    def __init__(self, episodes: list):
        self.episodes: list[Episode] = []
        self.series: list[Series] = []
        self._parse(episodes)

    def __getitem__(self, index: int):
        return self.series[index]

    def __iter__(self):
        return iter(self.series)

    def __len__(self):
        return len(self.series)

    def _parse(self, episodes: list):
        grouped = defaultdict(list)

        for item in episodes:
            episode = Episode(**item)
            grouped[episode.series].append(episode)
            self.episodes.append(episode)

        for x, item in enumerate(grouped.values(), start=1):
            self.series.append(Series(number=x, episodes=item))


@dataclasses.dataclass
class Series:
    number: int
    episodes: list

    def __getitem__(self, index: int):
        return self.episodes[index]

    def __iter__(self):
        return iter(self.episodes)

    def __len__(self):
        return len(self.episodes)

    @property
    def episodes_with_comments(self):
        return [
            item
            for item in self
            if item.has_episode_comments or item.has_track_comments
        ]


@dataclasses.dataclass
class SpotifyArtist:
    id: str
    name: str


@dataclasses.dataclass
class SpotifyData:
    id: str
    url: str
    name: str
    artists: list[SpotifyArtist]
    released: str

    def __post_init__(self):
        self.artists = [SpotifyArtist(**item) for item in self.artists]


@dataclasses.dataclass
class Track:
    _name: str
    number: int
    artist: str
    chosen_by: str
    spotify: SpotifyData | None
    youtube: Optional[str] = None
    connection: Optional[str] = None
    timestamp: Optional[str] = None
    comments: Optional[str] = None

    def __post_init__(self):
        if self.spotify is not None:
            self.spotify = SpotifyData(**self.spotify)

    @property
    def is_first(self):
        return self.number == 1

    @property
    def spotify_id(self):
        if self.spotify is not None and self.spotify.id is not None:
            return self.spotify.id
        else:
            return None

    @property
    def has_media_link(self):
        return bool(self.spotify_id or self.youtube)

    @property
    def has_comments(self):
        return self.comments is not None

    @property
    def artists(self):
        if self.spotify is not None and self.spotify.artists:
            return [artist.name for artist in self.spotify.artists]
        elif self.artist is not None:
            return [self.artist]
        else:
            return None

    @property
    def name(self):
        if self.spotify is not None and self.spotify.name is not None:
            return self.spotify.name
        else:
            return self._name


@dataclasses.dataclass
class Episode:
    id: str
    url: str
    playlist_tracks: list
    other_tracks: list
    series: int
    episode: int
    broadcast: str
    one_off_special: bool = False
    comments: Optional[str] = None

    def __post_init__(self):
        playlist_tracks = []

        for x, item in enumerate(self.playlist_tracks, start=1):
            track = Track(
                _name=item.get("name"),
                number=x,
                artist=item.get("artist"),
                chosen_by=item.get("chosen_by"),
                spotify=item.get("spotify"),
                youtube=item.get("youtube"),
                connection=item.get("connection"),
                timestamp=item.get("timestamp"),
                comments=item.get("comments"),
            )
            playlist_tracks.append(track)

        self.playlist_tracks = playlist_tracks

    def __getitem__(self, index: int):
        return self.playlist_tracks[index]

    def __iter__(self):
        return iter(self.playlist_tracks)

    @property
    def number(self):
        return self.episode

    @property
    def track_count(self):
        return len(self.playlist_tracks)

    @property
    def is_first(self):
        return self.episode == 1

    @property
    def has_episode_comments(self):
        return self.comments is not None

    @property
    def has_track_comments(self):
        for track in self.playlist_tracks:
            if track.has_comments:
                return True
        return False


@dataclasses.dataclass
class PresenterLeaderboardRow:
    date: str
    series: int
    episode: int
    track: Track

    @property
    def name(self):
        return self.track.chosen_by
