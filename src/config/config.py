# @ metadata

# = name: Circles and rectangles
# = background: #121212
# = width: 1280
# = height: 720

# @ timeline

# @@ 00:00:00 - 00:05:00

# = animation: top-to-bottom
# = item: shape
#   + shape: circle
#   + cx: 10
#   + cy: 10
#   + radius: 40

import json


class Config:
    def __init__(self):
        self.config = {}

        self.config["metadata"] = {}
        self.config["timeline"] = []

        self.scope = "none"
        self.time_slot_index = -1

    def tokenize(self, line, delimiter):
        return line.split(delimiter)

    def add_tokens(self, prop=None, value=None):
        if self.scope == "metadata":
            metadata = self.config["metadata"]
            metadata[prop] = value

        elif self.scope == "timeline":
            timeline = self.config["timeline"]
            time_slot = timeline[self.time_slot_index]

            time_slot[prop] = value

    def parse_config(self, config_file=None):
        with open(config_file, "r") as file:
            for line in file.readlines():
                if len(line.strip()) == 0:
                    continue

                tokens = self.tokenize(line, " ")

                if tokens[-1].strip() == "metadata":
                    self.scope = "metadata"
                    continue
                elif tokens[-1].strip() == "timeline":
                    self.scope = "timeline"
                    continue

                if tokens[0] == "@@":
                    self.time_slot_index += 1
                    time_start = self.tokenize(line, " ")[1].strip()
                    time_end = self.tokenize(line, " ")[-1].strip()

                    timeline = self.config["timeline"]
                    timeline.append({})

                    time_slot = timeline[self.time_slot_index]

                    time_slot["time_start"] = time_start
                    time_slot["time_end"] = time_end

                elif self.scope != "none":
                    if self.tokenize(line, " ")[0] == ">":
                        timeline = self.config["timeline"]
                        time_slot = timeline[self.time_slot_index]

                        time_slot["item"] = {}
                        time_slot["item"]["name"] = self.tokenize(line, " ")[-1].strip()
                        continue

                    if self.tokenize(line.strip(), " ")[0] == "+":
                        prop = self.tokenize(line.strip(), ":")[0].strip()
                        prop = self.tokenize(prop, " ")[-1].strip()

                        value = self.tokenize(line.strip(), ":")[-1].strip()

                        timeline = self.config["timeline"]
                        time_slot = timeline[self.time_slot_index]

                        time_slot["item"][prop] = value
                        continue

                    prop = self.tokenize(line, ":")[0].strip()
                    prop = self.tokenize(prop, " ")[-1].strip()

                    value = self.tokenize(line, ":")[-1].strip()

                    self.add_tokens(prop, value)

        with open("config.json", "w") as file:
            file.write(json.dumps(self.config))
        return self.config
