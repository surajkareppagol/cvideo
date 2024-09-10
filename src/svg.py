class SVG:
    def __init__(self):
        self.width = 1080
        self.height = 1920

        self.create_template()

        self.elements = []

    def create_template(self):
        self.svg_boilerplate = f"""
            <svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">
              <%CODE%>
            </svg>
          """

    def set_page_size(self,  width=1080, height=1920):
        self.width = width
        self.height = height

        self.create_template()

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
          stroke : Stroke Color
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

    def rectangle(self, xcor, ycor, width, height, rx=0, ry=0, fill = "#000", stroke = "#000", **extras):
        """
        Rectangle <rect /> and add it to list of elements.

        Arguments:
          xcor   : x co-ordinate (x)
          ycor   : y co-ordinate (y)
          width  : Width
          height : Height
          rx     : Corner Radius
          ry     : Corner Radius
          fill   : Fill Color
          stroke : Stroke Color
          extras : Extra arguments "stoke_width (float)"
        """
        element = "<rect "

        element += f"x=\"{xcor}\" "
        element += f"y=\"{ycor}\" "
        element += f"width=\"{width}\" "
        element += f"height=\"{height}\" "
        element += f"rx=\"{rx}\" "
        element += f"ry=\"{ry}\" "
        element += f"fill=\"{fill}\" "
        element += f"stroke=\"{stroke}\" "

        for key, value in extras.items():
          if element == "stroke_width":
            element += f"{element.replace("_", "-")}=\"{value}\" "

        element += "/> "

        self.elements.append(element)
