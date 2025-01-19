class VDParser:
    def __init__(self) -> None:
        self.config: dict = {}

        self.config["metadata"] = {}
        self.config["timeline"] = []

        self.METADATA = "metadata"
        self.TIMELINE = "timeline"

    def parse(self, file: str) -> str:
        # Collect all lines
        with open(file, "r") as file:
            lines: list = file.readlines()

        config_metadata = self.config["metadata"]
        config_timeline = self.config["timeline"]

        block: str = None

        for line in lines:
            tokens = line.strip().split(" ")
            symbol = tokens[0]

            # Read block header
            if symbol == "@":
                # Debug: ['@', 'metadata']

                block = (
                    self.METADATA
                    if tokens[-1].strip() == self.METADATA
                    else self.TIMELINE
                )

                continue

            # Read metadata
            if symbol == "+":
                # Debug: ['+', 'width:', '1280']

                prop = tokens[1].strip()[:-1]
                value = " ".join(tokens[2:]).strip()

                # Add property and value
                if block == self.METADATA:
                    config_metadata[prop] = value
                elif block == self.TIMELINE:
                    timeline["components"][-1][prop] = value

                continue

            # Read timeline with @@
            if symbol == "@@":
                # Debug:  ['@@', '00:00:00', '-', '00:00:05']

                config_timeline.append({})

                timeline = config_timeline[-1]

                timeline["start"] = tokens[1].strip()
                timeline["end"] = tokens[-1].strip()
                timeline["components"] = []

                continue

            # Read items with >
            if symbol == ">":
                # Debug: ['>', 'item:', 'shape']

                timeline["components"].append({})
                value = " ".join(tokens[2:]).strip()

                # Add property and value
                timeline["components"][-1]["item"] = value

                continue

        return self.config
