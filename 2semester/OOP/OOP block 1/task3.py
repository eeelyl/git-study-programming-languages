class Calc:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value


a = Calc(3)
b = Calc(4)
print('{} + {} = {}'.format(a.value, b.value, a + b))
print('{} - {} = {}'.format(a.value, b.value, a - b))
print('{} * {} = {}'.format(a.value, b.value, a * b))
print('{} / {} = {}'.format(a.value, b.value, a / b))
