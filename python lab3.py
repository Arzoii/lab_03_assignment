class Shape:
    def _init_(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Rectangle(Shape):
    def _init_(self, width, height, color):
        super()._init_(color)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Circle(Shape):
    def _init_(self, radius, color):
        super()._init_(color)
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

rect = Rectangle(10, 20, "red")
print("Rectangle color:", rect.get_color())
print("Rectangle area:", rect.get_area())

circle = Circle(5, "blue")
print("Circle color:", circle.get_color())
print("Circle area:", circle.get_area())

