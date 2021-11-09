from src.figure import Figure
import math

def exist_size(*args):
    for arg in args:
        if not isinstance(arg, (float, int)):
            raise ValueError('size not float or int')
        if arg <= 0:
            raise ValueError('size </= 0')

class Triangle(Figure):
    name = "Triangle"

    @staticmethod
    def exist_triangle(size_1, size_2, size_3):
        if  size_1 + size_2 > size_3 and size_1 + size_3 > size_2 and size_2 + size_3 > size_1:
            return size_1, size_2, size_3
        else:
            raise ValueError('triangle is not exist')

    def __new__(cls, size_a, size_b, size_c):
        exist_size(size_a, size_b, size_c)
        if cls.exist_triangle(size_a, size_b, size_c):
            instance = super(Triangle, cls).__new__(cls)
            instance.size_a = size_a
            instance.size_b = size_b
            instance.size_c = size_c
            return instance
        else:
            return None

    @property
    def area(self):
        p = (self.size_c + self.size_b + self.size_a) / 2
        return math.sqrt(p*(p-self.size_a)*(p-self.size_b)*(p-self.size_c))

    @property
    def perimeter(self):
        return self.size_a + self.size_b + self.size_c


