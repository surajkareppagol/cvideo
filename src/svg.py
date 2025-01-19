from os import path


class SVG:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.elements = []

        self.svg = """
            <svg width="<%WIDTH%>" height="<%HEIGHT%>" xmlns="http://www.w3.org/2000/svg">
            <%CODE%>
            </svg>"""

    def background(self, bg_color="#fff"):
        background = f"""
            <rect x="0" y="0" width="<%WIDTH%>" height="<%HEIGHT%>" fill="{bg_color}" />"""
        self.elements.append(background)

    def create_element(self, item, **kwargs):
        components = {"circle": "circle", "rectangle": "rect"}

        if item in components.keys():
            shape = f"<{components[item]} "
        else:
            return

        for prop, value in kwargs.items():
            shape += f'{prop}="{value}" '

        shape += "/> "

        self.elements.append(shape)

    def create_svg(self, svg_file, svg_dir="svg"):
        svg = self.svg.replace("<%CODE%>", "".join(self.elements))

        svg = svg.replace("<%WIDTH%>", self.width)
        svg = svg.replace("<%HEIGHT%>", self.height)

        file = path.join(svg_dir, svg_file)

        with open(file, "w") as file:
            file.write(svg)

        self.elements.clear()
