from sys import exit, argv
from parser import Parser
from svg import SVG_
from convert import image_to_video

from shutil import rmtree
import time
import os

total_time: int = 0
total_frames: int = 0

config: dict = {}
svg = None


def calculate_frames(end_time: int | float, frame_rate: int = 30) -> int:
    global total_time

    time_tuple = time.strptime(end_time, "%H:%M:%S")

    total_seconds = (
        time_tuple.tm_sec + (time_tuple.tm_min * 60) +
        (time_tuple.tm_hour * 3600)
    )

    frames = (total_seconds - total_time) * frame_rate

    total_time += total_seconds

    return frames


def create_svg(time_slot: dict, frames: int) -> None:
    global total_frames, svg

    items = time_slot["items"]

    movement = 1

    for frame in range(total_frames, total_frames + frames):
        # Set background
        svg.set_background()

        for item in items:
            speed = item["speed"]
            shape = item["shape"]

            if shape == "circle":
                cx = item["cx"]
                cy = item["cy"]
                radius = item["radius"]

                svg.create_element("circle", cx=cx, cy=int(
                    cy) * movement, r=radius, fill="#c17261", stroke="#fff")

            elif shape == "rectangle":
                x = item["x"]
                y = item["y"]
                width = item["width"]
                height = item["height"]

                svg.create_element("rectangle", x=x, y=int(y) + movement, width=width,
                                   height=height, fill="#fff", rx="0", ry="0", stroke="#000")

            elif shape == "text":
                x = item["x"]
                y = item["y"]
                text = item["text"]

                svg.create_element("text", x=x, y=y, text=text, fill="#000")

            movement += int(speed)

        svg.create(output_file=f"{frame:06}.svg")

        total_frames += frames


def create_video() -> None:
    image_to_video(output="svvgb")


def main() -> None:
    global config, svg

    if len(argv) < 2:
        exit(1)

    file = argv[-1]
    config = Parser().parse(file)

    # Create svg folder to store svg
    if not os.path.exists("svg-dir"):
        os.mkdir("svg-dir")

    metadata = config["metadata"]
    timeline = config["timeline"]

    width = metadata["width"]
    height = metadata["height"]

    svg = SVG_(width, height)

    for time_slot in timeline:
        frames = calculate_frames(time_slot["end"])
        create_svg(time_slot, frames)

    create_video()
    rmtree("svg-dir")


if __name__ == "__main__":
    main()
