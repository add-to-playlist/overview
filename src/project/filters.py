from datetime import datetime

from project.models import Series, Track
from project.utils import SERIES_PLAYLIST_IDS


def date_format(value: str):
    dt = datetime.fromisoformat(value)
    return f"{dt.day} {dt.strftime("%B %Y")}"


def get_playlist_url(series: Series):
    return SERIES_PLAYLIST_IDS[series.number - 1]


def spotify_playlist_url(value: str):
    return f"https://open.spotify.com/playlist/{value}"


def media_link(track: Track):
    if track.spotify_id is not None:
        return f"https://open.spotify.com/track/{track.spotify_id}"
    elif track.youtube is not None:
        return track.youtube
    else:
        raise Exception("Unknown media link")


def table_class_name(number: int):
    return "td-even" if (number % 2) == 0 else "td-odd"


filters = {
    "date_format": date_format,
    "get_playlist_url": get_playlist_url,
    "media_link": media_link,
    "spotify_playlist_url": spotify_playlist_url,
    "table_class_name": table_class_name,
}
