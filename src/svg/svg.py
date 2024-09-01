import cairosvg

class SVG:
    def __init__(self, width=1080, height=1920):
        self.svg_boilerplate = f"""
            <svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
              <%CODE%>
            </svg>
          """
        self.width = width
        self.height = height

        self.elements = []

    def create(self, svg_output="output.svg"):
        self.svg_output = svg_output
        svg_code = self.svg_boilerplate.replace("<%CODE%>", " ".join(self.elements))

        with open(svg_output, "w") as file:
            file.write(svg_code)

        self.elements = []

    def circle(self, xcor, ycor, radius, fill = "#000", stroke = "#000", **extras):
        """
        Create <circle /> and add it to list of elements.

        Arguments:
          xcor   : x co-ordinate
          ycor   : y co-ordinate
          radius : Radius
          fill   : Fill Color
          stroke  : Stroke Color
          extras : Extra arguments "stoke_width (float)"
        """

        element = "<circle "

        element += f"cx=\"{xcor}\" "
        element += f"cy=\"{ycor}\" "
        element += f"r=\"{radius}\" "
        element += f"fill=\"{fill}\" "
        element += f"stroke=\"{stroke}\" "

        for key, value in extras.items():
          if element == "stroke_width":
            element += f"{element.replace("_", "-")}=\"{value}\" "

        element += "/> "

        self.elements.append(element)

    def convert(self, png_output="output.png", format="png"):
      with open(self.svg_output, "r") as file:
        cairosvg.svg2png(file_obj=file, write_to=f"{png_output}")
