import ffmpeg


def image_to_video(
    output: str, video_format="mkv", source_dir: str = "svg-dir",
):
    image_glob = f"{source_dir}/*.svg"
    video_output = f"{output}.{video_format}"

    ffmpeg.input(image_glob, pattern_type="glob", framerate=30).output(
        video_output, loglevel="quiet"
    ).run(overwrite_output=True)
