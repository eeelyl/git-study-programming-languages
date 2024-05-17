def super_function(func1, func2):
    def inner(x):
        return func1(func2(x))
    return inner

# Пример использования:


def add(x):
    return x + 10


def multiply(x):
    return x * 5


print(super_function(add, float)('16'))
print(super_function(tuple, multiply)((3, 4, 5)))
print(super_function(str, multiply)('55'))
print(super_function(list, multiply)((1, 2, 3)))
