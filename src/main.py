from svg.svg import SVG
from convert.convert import Convert

svg = SVG()

# A circle moving down from top
# 30 frames / second

# Width 1080

frames = 300  # 300 / 30 = 10

for i in range(1, frames):
    svg.circle(1080 // 2 - 100, i, "200", "#fff", "#fff")
    svg.create(svg_output=f"{i:04}.svg")
    svg.convert(png_output=f"{i:04}.png")

convert = Convert()

convert.image_to_video(source_dir=".")
