import math


class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p*(p-self.side_a)*(p-self.side_b)*(p-self.side_c))


crc = Circle(3)
sqr = Square(3)
tr = Triangle(3, 4, 5)
print('Периметр круга = {}, площадь круга = {}'.format(
    crc.area(), crc.perimeter()))
print('Площадь квадрата = {}, периметр квадрата = {}'.format(
    sqr.area(), sqr.perimeter()))
print('Площадь треугольника = {}, периметр треугольника = {}'.format(
    tr.area(), tr.perimeter()))
