class Parser:
    def __init__(self) -> None:
        self.config: dict = {}

    def read_file(self, file: str) -> list[str]:
        with open(file, "r") as file:
            return file.readlines()

    def parse(self, file: str) -> str:
        lines: list = self.read_file(file)

        self.config["metadata"] = {}
        self.config["timeline"] = []

        config_metadta = self.config["metadata"]
        config_timeline = self.config["timeline"]

        current_timeline: dict = {}
        current_timeline_index: int = -1

        current_item: dict = {}
        current_item_index: int = -1

        level: str = None

        for line in lines:
            tokens = line.strip().split(" ")
            symbol = tokens[0]

            # Read metadata and timeline with @
            if symbol == "@":
                level = "metadata" if tokens[-1].strip(
                ) == "metadata" else "timeline"
                continue

            # Read data with =
            if symbol == "=" and level == "metadata":
                prop = tokens[1].strip()[:-1]
                value = " ".join(tokens[2:]).strip()

                # Add property and value
                config_metadta[prop] = value

                continue

            # Read timeline with @@
            if symbol == "@@":
                current_timeline_index += 1
                current_item_index = -1

                config_timeline.append({})

                # Get current timeline from the list
                timeline = config_timeline[current_timeline_index]

                timeline["start"] = tokens[1].strip()
                timeline["end"] = tokens[-1].strip()

                timeline["items"] = []

                current_item = timeline["items"]
                continue

            # Read data with =
            if symbol == "=" and level == "timeline":
                prop = tokens[1].strip()[:-1]
                value = " ".join(tokens[2:]).strip()

                # Add property and value
                timeline[prop] = value

                continue

            # Read items with >
            if symbol == ">":
                current_item_index += 1
                current_item.append({})

                value = " ".join(tokens[2:]).strip()

                # Add property and value
                current_item[current_item_index]["name"] = value

                continue

            # Read items data with +
            if symbol == "+":
                prop = tokens[1].strip()[:-1]
                value = " ".join(tokens[2:]).strip()

                # Add property and value
                current_item[current_item_index][prop] = value

                continue

        return self.config
