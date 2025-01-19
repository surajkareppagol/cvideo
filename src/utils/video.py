from os import path

import ffmpeg


def util_create_video(
    output="cvideo.mkv",
    source="svg",
):
    glob = path.join(source, "*.svg")

    ffmpeg.input(glob, pattern_type="glob", framerate=30).output(
        output, loglevel="quiet"
    ).run(overwrite_output=True)
