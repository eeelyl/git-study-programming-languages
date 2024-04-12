# Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(),
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные: название анализируемой функции,
# наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).
# Попробуйте повторить результат девушки.

import inspect


def inspect_function(func):
    func_name = func.__name__
    func_params = inspect.signature(func).parameters
    print(f"Название функции: {func_name}")
    for param_name, param in func_params.items():
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else "Не указан"
        param_kind = param.kind.name
        print(f"Параметр: {param_name}, Тип: {
              param_type}, Категория: {param_kind}")
# Пример функции для анализа


def example_function(var1: int, var2: str, *, var3: float = 0.0):
    pass


inspect_function(example_function)
