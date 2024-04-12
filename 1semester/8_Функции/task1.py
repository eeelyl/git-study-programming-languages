# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum_range(start, end):
    if start > end:
        start, end = end, start
    sum = 0
    for num in range(start, end+1):
        sum += num
    return sum


start = int(input("Введите значение start: "))
end = int(input("Введите значение end: "))
print(f'Сумма чисел от {start} до {end} равна {sum_range(start, end)}')
