def my_reduce(func, iterable, initializer):
    """Функция-агрегатор аналог встроенной reduce()."""
    accumulator = initializer
    for item in iterable:
        accumulator = func(accumulator, item)
    return accumulator

# Примеры функций для сложения и умножения


def add(x, y):
    return x + y


def mult(x, y):
    return x * y

# Пример использования


def main():
    input_str = input("Введите список чисел, разделенных пробелами: ")
    my_list = list(map(int, input_str.split()))

    sum_result = my_reduce(add, my_list, 0)
    mult_result = my_reduce(mult, my_list, 1)

    print(sum_result)
    print(mult_result)


if __name__ == "__main__":
    main()
