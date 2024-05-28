import time
import tracemalloc


def performance_decorator(func):
    def wrapper(*args, **kwargs):
        # Начало измерения времени
        start_time = time.time()

        # Начало измерения памяти
        tracemalloc.start()

        result = func(*args, **kwargs)

        # Завершение измерения памяти
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Завершение измерения времени
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Название функции: {func.__name__}")
        print(f"Текущее потребление памяти: {current / 10**6:.6f} мб")
        print(f"Пик использования памяти: {peak / 10**6:.6f} мб")
        print(f"Операция заняла: {elapsed_time:.6f} секунд")
        print(f"Функция {func.__name__} завершила работу")
        print("-" * 48)

        return result

    return wrapper


@performance_decorator
def make_list_with_range():
    res = list(range(1000000))


@performance_decorator
def make_list_comprehension():
    res = [i for i in range(1000000)]


@performance_decorator
def make_list_with_append():
    res = []
    for i in range(1000000):
        res.append(i)


@performance_decorator
def make_list_concatenation():
    res = []
    for i in range(100000):
        res += [i]


print(make_list_with_range())
print(make_list_comprehension())
print(make_list_with_append())
print(make_list_concatenation())
