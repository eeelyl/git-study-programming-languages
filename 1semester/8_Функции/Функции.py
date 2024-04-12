#Задание 1
def sum_range(start, end):
    if start > end:
        start, end = end, start
    sum = 0
    for num in range(start, end+1):
        sum += num
    return sum
start = int(input("Введите значение start: "))
end = int(input("Введите значение end: "))
result = sum_range(start, end)
print("Сумма чисел от", start, "до", end, "включительно равна:", result)

#Задание 2
def func1():  #во внутренней функции пользуемся внешней переменной, она не доступна. Функцию inner() не вызываем, поэтому ошибка не выдается
    param = 4
    def inner():
        param += 1
    return param
 
def func2():  #внутренняя функция увеличивает значение переменной на единицу, но сама ничего не возвращает, поэтому значение параметра не меняется
    param = 4 
    def inner(var):
        var += 1
    inner(param)
    return param
 
def func3():  #данная функция работает корректно (возвращает 5), т.к. во внутренней функции увеличивается внешняя переменная и присваивается результат в func3
    param = 4
    def inner(var):
        var += 1
        return var
    param = inner(param)
    return param

print(func1())
print(func2())
print(func3())

#Задание 3
def three_args(*, var1, var2 = None, var3 = None):  #задаем ограничение на тип переменных (их может быть только от одной от трех)
    arguments = ', '.join([f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])  #функция locals в виде словаря представляет внутренние аргументы функции
    print(f'Переданы аргументы: {arguments}')
three_args(var1=11)
three_args(var1='Hello', var3=1)
three_args(var1='Cold', var2=2, var3=77)

#Задание 4
from datetime import datetime
from time import sleep
def time_now(msg, *, dt = None):
    dt = dt or datetime.now() #вызываем значение текущего времени при выполнении функции, а не при ее создании (в случае необходимости параметра dt присваиваем ему None изначально)
    print(msg, dt)
time_now('Сейчас такое время: ')
sleep(1)
time_now('Прошла секунда: ')
sleep(1)
time_now('Задам другую дату: ', dt = '2019-11-07 15:06:12')

#Задание 5
import inspect #функционал для анализа объектов в Python, включая функции
def inspect_function(func):
    func_name = func.__name__
    func_params = inspect.signature(func).parameters
    print(f"Название функции: {func_name}")
    for param_name, param in func_params.items():  #выводим информацию о параметрах функции
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else "Не указан"
        param_kind = param.kind.name
        print(f"Параметр: {param_name}, Тип: {param_type}, Категория: {param_kind}")
#Пример функции для анализа
def example_function(var1: int, var2: str, *, var3: float = 0.0):
    pass
inspect_function(example_function)