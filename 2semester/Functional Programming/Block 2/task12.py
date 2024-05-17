import time
import psutil
import functools


def measure_performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_mem = psutil.virtual_memory().used
        result = func(*args, **kwargs)
        end_time = time.time()
        end_mem = psutil.virtual_memory().used
        print(f"Название функции: {func.__name__}")
        print(f"Использованный метод: {func.__doc__}")
        print(
            f"Текущее потребление памяти: {(end_mem - start_mem) / (1024 * 1024):.6f} мб")
        print(
            f"Пик использования памяти: {psutil.virtual_memory().max / (1024 * 1024):.6f} мб")
        print(f"Операция заняла: {end_time - start_time:.6f} секунд")
        print(f"Функция {func.__name__} завершила работу")
        print("------------------------------------------------")
        return result
    return wrapper


@measure_performance
def make_list_with_range():
    """
    range()
    """
    return list(range(1000000))


@measure_performance
def make_list_comprehension():
    """
    list comprehension
    """
    return [i for i in range(1000000)]


@measure_performance
def make_list_with_append():
    """
    append()
    """
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst


@measure_performance
def make_list_concatenation():
    """
    concatenation
    """
    lst = []
    for i in range(1000000):
        lst += [i]
    return lst


print(make_list_with_range())
print(make_list_comprehension())
print(make_list_with_append())
print(make_list_concatenation())
