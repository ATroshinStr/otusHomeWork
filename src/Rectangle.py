from src.figure import Figure

class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, size_a, size_b):
        super().__init__(size_a, size_b)
        self.size_a = size_a
        self.size_b = size_b

    @property
    def area(self):
        return self.size_a * self.size_b

    @property
    def perimeter(self):
        return 2 * (self.size_a + self.size_b)

rectangle = Rectangle(5)