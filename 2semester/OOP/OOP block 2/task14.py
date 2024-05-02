from functools import total_ordering


@total_ordering
class RealString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self) == len(other)
        elif isinstance(other, str):
            return len(self) == len(other)
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self) < len(other)
        elif isinstance(other, str):
            return len(self) < len(other)
        else:
            return NotImplemented

    def __repr__(self):
        return f"RealString('{self.string}')"


# Пример использования
string1 = RealString("Apple")
string2 = RealString("Яблоко")
string3 = "Banana"

print(string1 == string2)  # Сравнение объектов RealString
print(string1 > string2)   # Сравнение объектов RealString
print(string1 < string3)   # Сравнение объекта RealString и строки
