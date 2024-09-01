import ffmpeg
from os import path


class Convert:
    def __init__(self):
        pass

    def image_to_video(
        self, output="output", source_dir=None, image_format="png", video_format="mkv"
    ):
        if source_dir is None:
            print("Convert: Source directory not found.")
            return

        image_glob = f"{source_dir}/*.{image_format}"
        video_output = f"{output}.{video_format}"

        ffmpeg.input(image_glob, pattern_type="glob", framerate=30).output(
            video_output
        ).run(overwrite_output=True)
