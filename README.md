# SVVGB

🎬 `SVVGB` is a video builder tool. It uses a configuration file to read the sequence of commands and creates a svg file.

The `SVG` files are combined together via `ffmpeg-python` module.

## ⚙️ Installation and usage

```bash
git clone https://github.com/surajkareppagol/svvgb.git
cd svvgb
```

```bash
python3 -m venv venv
source ./venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python3 src/main.py [config-file]
```

## 👷 Config format

```bash
@ metadata

= name: Circles and rectangles
= background: #c17261
= width: 1280
= height: 720

@ timeline

@@ 00:00:00 - 00:00:05

> item: shape
  + shape: circle
  + cx: 600
  + cy: 12
  + radius: 400
  + speed: 2
> item: shape
  + shape: rectangle
  + x: 600
  + y: 12
  + width: 400
  + height: 200
  + speed: 2

@@ 00:00:06 - 00:00:10

> item: shape
  + shape: rectangle
  + x: 600
  + y: 12
  + width: 400
  + height: 200
  + speed: 6
> item: shape
  + shape: text
  + x: 600
  + y: 12
  + text: SVVGB - SVG to Video
  + speed: 4
```

- Format is divided into two sections `metadata` and `timeline`
- This sections are preceded with `@` and time slots are preceded with `@@`.
- Each of the attribute starts with `=` and it is in the above format.
- Nested item starts with `>` with all the child items `+`.

## ☰ Available shapes and options

### Metadata

- Name
- Background color
- Width
- Height

### Timeline

- Shapes
  - Circle
  - Rectangle
  - Text
- speed (integer, default: 2)

## ✨ Features

- Create svg via SVG class
- Easy to use API
- Uses `ffmpeg` so multiple video formats available
- Easy to use configuration format

## ✅ To do

- Add more features to configuration file
- Add more parser rules to configuration file
- Add more elements to SVG class
