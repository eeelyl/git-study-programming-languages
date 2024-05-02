class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


x = Point(1, 2)
y = Point(3, 4)
print(x + y)
