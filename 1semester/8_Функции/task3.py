# Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
# В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None.
# Получим, например, следующее сообщение: Переданы аргументы: var1 = 2, var3 = 10.

def three_args(*, var1, var2=None, var3=None):
    arguments = ', '.join(
        [f'{arg[0]} = {str(arg[1])}' for arg in locals().items() if arg[1] is not None])
    print(f'Переданы аргументы: {arguments}')


three_args(var1=1)
three_args(var1='Test', var3=3)
three_args(var1='Test', var2=2, var3=3)
