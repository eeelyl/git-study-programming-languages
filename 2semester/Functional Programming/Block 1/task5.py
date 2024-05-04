def func(n):
    if n == 203:
        return 1
    elif n > 203:
        return 0
    else:
        return func(n + 1) + func(n * 3)

# Пример использования
n = 1
print("Число вариантов достижения числа 203 от числа", n, ":", func(n))
