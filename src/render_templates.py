import hashlib
import json
import os

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from project.filters import filters
from project.models import SeriesCollection
from project.utils import (
    ALL_PLAYLIST_ID,
    get_artist_leaderboard,
    get_presenter_leaderboard,
)

EPISODE_DATA_PATH = os.environ.get("EPISODE_DATA_PATH", "data.json")
OUTPUT_HTML_PATH = os.environ.get("OUTPUT_HTML_PATH", "../assets/index.html")


def load_series_data():
    with open(
        EPISODE_DATA_PATH,
        mode="r",
        encoding="utf8",
    ) as f:
        return SeriesCollection(episodes=json.load(f))


def main():
    env = Environment(
        loader=FileSystemLoader("templates"),
        undefined=StrictUndefined,
        lstrip_blocks=True,
        trim_blocks=True,
    )

    env.filters.update(filters)
    env.globals["TABLE_CLASSES"] = "striped"

    template = env.get_template("index.j2")

    all_series = load_series_data()

    artist_leaderboard_amt = 25
    artist_leaderboard = get_artist_leaderboard(
        all_series=all_series,
        amount=artist_leaderboard_amt,
    )

    presenter_leaderboard_amt = 10
    presenter_leaderboard = get_presenter_leaderboard(
        all_series=all_series,
        amount=presenter_leaderboard_amt,
    )

    bar_chart_labels = [", ".join(item["names"]) for item in artist_leaderboard]
    bar_chart_data = [item["count"] for item in artist_leaderboard]
    bar_chart_tracks = [
        [f"S{t['series']:02}E{t['episode']:02} - {t['name']}" for t in item["tracks"]]
        for item in artist_leaderboard
    ]

    with open("../assets/styles.css", "rb") as f:
        styles_hash = hashlib.sha256(f.read()).hexdigest()[:12]

    output = template.render(
        all_series=all_series,
        all_series_playlist=ALL_PLAYLIST_ID,
        artist_leaderboard=artist_leaderboard,
        artist_leaderboard_amt=artist_leaderboard_amt,
        bar_chart_data=bar_chart_data,
        bar_chart_labels=bar_chart_labels,
        bar_chart_tracks=bar_chart_tracks,
        styles_hash=styles_hash,
        max_visible_artists=3,
        max_visible_picks=5,
        presenter_leaderboard=presenter_leaderboard,
        presenter_leaderboard_amt=presenter_leaderboard_amt,
    )

    with open(OUTPUT_HTML_PATH, mode="w", encoding="utf8") as f:
        f.write(output)


if __name__ == "__main__":
    main()
