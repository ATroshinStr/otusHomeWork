from src.figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"

    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def area(self):
        return pi * (self.size ** 2)

    @property
    def perimeter(self):
        return 2 * self.size * pi

circle = Circle(2)

print(circle.area)
