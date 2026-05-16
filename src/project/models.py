import dataclasses

from collections import defaultdict


class SeriesCollection:
    def __init__(self, episodes: list):
        self.episodes = []
        self.series = []
        self._parse(episodes)

    def __getitem__(self, index):
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

        for x, item in enumerate(grouped.values()):
            self.series.append(Series(number=x + 1, episodes=item))


@dataclasses.dataclass
class Series:
    number: int
    episodes: list

    def __getitem__(self, index):
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
class Episode:
    id: str
    url: str
    playlist_tracks: list
    other_tracks: list
    series: int
    episode: int
    broadcast: str
    one_off_special: bool = False
    comments: str | None = None

    def __post_init__(self):
        playlist_tracks = []

        for x, item in enumerate(self.playlist_tracks):
            track = Track(
                _name=item.get("name"),
                number=x + 1,
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

    def __getitem__(self, index):
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
class Track:
    _name: str
    number: int
    artist: str
    chosen_by: str
    spotify: dict
    youtube: str | None = None
    connection: str | None = None
    timestamp: str | None = None
    comments: str | None = None

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
class SpotifyData:
    id: str
    url: str
    name: str
    artists: list
    released: str

    def __post_init__(self):
        self.artists = [SpotifyArtist(**item) for item in self.artists]


@dataclasses.dataclass
class SpotifyArtist:
    id: str
    name: str


@dataclasses.dataclass
class PresenterLeaderboardRow:
    date: str
    series: int
    episode: int
    track: Track

    @property
    def name(self):
        return self.track.chosen_by
