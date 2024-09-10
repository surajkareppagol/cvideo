from svg.svg import SVG
from convert.convert import Convert

from rich.console import Console
from rich.panel import Panel

import json
from sys import argv

import time
import os

from config.config import Config

term = Console()
convert = Convert()
svg = SVG()

current_time = 0


def calculate_frames(time_end, frame_rate=30):
    global current_time

    time_e_tuple = time.strptime(time_end, "%H:%M:%S")

    total_e_seconds = (
        time_e_tuple.tm_sec + (time_e_tuple.tm_min * 60) + (time_e_tuple.tm_hour * 3600)
    )

    frames = (total_e_seconds - current_time) * frame_rate

    current_time += total_e_seconds

    return frames


def create_svg(video_data, frames):
    shape_data = video_data["item"]

    shape = shape_data["shape"]

    if not os.path.exists("svvgb_svg"):
        os.mkdir("svvgb_svg")

    for i in range(1, frames):
        if shape == "circle":
            cx = shape_data["cx"]
            cy = shape_data["cy"]
            radius = shape_data["radius"]

            svg.circle(cx, int(cy) * i, radius, "#fff", "#fff")

        svg.create(svg_output=f"svvgb_svg/{i:04}.svg")


def create_video():
    convert.image_to_video(source_dir="svvgb_svg")


def main():
    term.print(
        Panel.fit("[bold green]SVVGB (SVG to Video Builder)[/bold green]"),
        justify="center",
    )

    config = Config().parse_config(argv[-1])

    term.print("🙂 Config file parsed successfully...\n")

    metadata = config["metadata"]
    timeline = config["timeline"]

    for time_slot in timeline:
        frames = calculate_frames(time_slot["time_end"])
        create_svg(time_slot, frames)

        with term.status("⚙️  Creating Video", spinner="arc"):
            create_video()

        term.print("🚀 Video has been created.")


if __name__ == "__main__":
    main()
