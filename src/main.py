import time
from json import dumps
from os import mkdir, path
from shutil import rmtree
from sys import argv, exit

from console import console
from svg import SVG
from utils.args import util_parse_cmd_args, util_print_help
from utils.video import util_create_video
from vdparser import VDParser

total_time = 0
start_frame = 0

svg = None


def calculate_frames(end_time, frame_rate=30):
    # Total seconds * frames
    global total_time

    time_tuple = time.strptime(end_time, "%H:%M:%S")

    total_seconds = (
        time_tuple.tm_sec + (time_tuple.tm_min * 60) + (time_tuple.tm_hour * 3600)
    )

    frames = (total_seconds - total_time) * frame_rate

    total_time += total_seconds

    return frames


def create_svg(time_slot, frames):
    global start_frame, svg

    items = time_slot["components"]

    # Here adding start_frame just for filenames, actually generating only
    # frames

    movement = 1

    for frame in range(start_frame, start_frame + frames):
        # Set background
        svg.background()

        for item in items:
            speed = item["speed"]
            shape = item["shape"]

            if shape == "circle":
                cx = item["cx"]
                cy = item["cy"]
                radius = item["radius"]

                svg.create_element(
                    "circle",
                    cx=cx,
                    cy=int(cy) * movement,
                    r=radius,
                    fill="#c17261",
                    stroke="#fff",
                )

            elif shape == "rectangle":
                x = item["x"]
                y = item["y"]
                width = item["width"]
                height = item["height"]

                svg.create_element(
                    "rectangle",
                    x=x,
                    y=int(y) + movement,
                    width=width,
                    height=height,
                    fill="#fff",
                    rx="0",
                    ry="0",
                    stroke="#000",
                )

            elif shape == "text":
                x = item["x"]
                y = item["y"]
                text = item["text"]

                svg.create_element("text", x=x, y=y, text=text, fill="#000")

            movement += int(speed)

        svg.create_svg(f"{frame:06}.svg")

        start_frame += frames


def main():
    global svg

    if len(argv) < 2:
        util_print_help()
        exit(1)

    args = util_parse_cmd_args()

    config = VDParser().parse(args.filename)

    if args.config:
        console.print_json(dumps(config))

    if not path.exists("svg"):
        mkdir("svg")

    metadata = config["metadata"]
    timeline = config["timeline"]

    width = metadata["width"]
    height = metadata["height"]

    svg = SVG(width, height)

    for time_slot in timeline:
        frames = calculate_frames(time_slot["end"])
        create_svg(time_slot, frames)

    util_create_video()
    rmtree("svg")


if __name__ == "__main__":
    main()
