from src.figure import Figure

class Square(Figure):
    name = "Square"

    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def area(self):
        return self.size ** 2

    @property
    def perimeter(self):
        return self.size * 4

square = Square(5)

sq = square.area

print(sq)