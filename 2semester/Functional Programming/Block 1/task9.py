import time

# Итеративное возведение в степень


def power_iterative(n, m):
    result = 1
    for _ in range(m):
        result *= n
    return result

# Рекурсивное возведение в степень


def power_recursive(n, m):
    if m == 0:
        return 1
    elif m % 2 == 0:
        return power_recursive(n * n, m // 2)
    else:
        return n * power_recursive(n, m - 1)


# Сравнение скорости выполнения обоих решений
n = 5
m = 100

start_time = time.time()
result_iterative = power_iterative(n, m)
end_time = time.time()
print(f"Результат итеративного возведения в степень: {result_iterative}")
print(f"Время выполнения итеративного подхода: {end_time - start_time} секунд")

start_time = time.time()
result_recursive = power_recursive(n, m)
end_time = time.time()
print(f"Результат рекурсивного возведения в степень: {result_recursive}")
print(f"Время выполнения рекурсивного подхода: {end_time - start_time} секунд")
