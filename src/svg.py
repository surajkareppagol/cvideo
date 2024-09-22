class SVG_:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.elements = []

        self.svg_code = f"<svg width=\"{width}\" height=\"{
            height}\" xmlns=\"http://www.w3.org/2000/svg\"><%CODE%></svg>"

    def set_background(self, background_color: str = "#ffffff"):
        # Create background color
        background = f"<rect x=\"0\" y=\"0\" width=\"{
            self.width}\" height=\"{self.height}\" fill=\"{background_color}\" />"
        self.elements.append(background)

    def create(self, output_file: str, output_dir: str = "svg-dir"):
        svg_code = self.svg_code.replace("<%CODE%>", "".join(self.elements))
        svg_file = f"{output_dir}/{output_file}"

        with open(svg_file, "w") as file:
            file.write(svg_code)

        self.elements = []

    def create_element(self, shape_: str, **kwargs):
        if shape_ == "circle":
            shape = "<circle "
        elif shape_ == "rectangle":
            shape = "<rect "
        elif shape_ == "text":
            shape = "<text <%PROPS%>><%TEXT%></text>"
            props = ""

            for prop, value in kwargs.items():
                if prop == "text":
                    continue

                props += f"{prop}=\"{value}\" "

            shape = shape.replace("<%PROPS%>", f"{props}")
            shape = shape.replace("<%TEXT%>", kwargs["text"])
            self.elements.append(shape)

            return

        for prop, value in kwargs.items():
            shape += f"{prop}=\"{value}\" "

        shape += "/> "

        self.elements.append(shape)
