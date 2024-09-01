# SVVGB

🎬 `SVVGB` is a video builder tool. It uses a configuration file to read the sequence of commands and creates a svg file.

This svg file is then converted to png via `cairosvg` module and then all the images are combined together via `ffmpeg-python` module.

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
python3 src/main.py
```

## ✨ Features

- Create svg via SVG class
- Easy to use API
- Uses `ffmpeg` so multiple video formats available

## ✅ To do

- Add the configuration file details
- Create a parser for configuration file
- Add more elements to SVG class
