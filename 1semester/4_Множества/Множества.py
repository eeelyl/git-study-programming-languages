#Задание 1
def to_set(element):
    st = set(element)
    return st, len(st)
print(to_set('введите текст'))
print(to_set([1,5,6,2,4,8,11,1,4,3,5,6]))

#Задание 2
#абстрактные базовые классы для контейнеров
from collections.abc import Hashable  #будем проверять каждый элемент на хэшируемость (преобразование массивы входных данных произвольной длины в выходную битовую строку установленной длины
def list_to_set(lst):
    st = {item for item in lst if isinstance(item, Hashable)}  #проверям,является ли объект хэшируемым 
    print(st)
print(list_to_set([1,[2],[3,4,5,6],11]))

#Задание 3
def diff(set1, set2, set3, symmetric = True):
    if symmetric:
        result = set1.symmetric_difference(set2).symmetric_difference(set3)
    else:
        result = set1.difference(set2).difference(set3)
    return result
set1 = set(input("Введите элементы первого множества через пробел: ").split())
set2 = set(input("Введите элементы второго множества через пробел: ").split())
set3 = set(input("Введите элементы третьего множества через пробел: ").split())
result1 = diff(set1, set2, set3)
print("Симметричная разность: ", result1)
result2 = diff(set1, set2, set3, symmetric = False)
print("Простая разность: ", result2)

#Задание 4
def superset(set1, set2):
    if set1 == set2:
        print("Множества равны")
    elif set1.issuperset(set2):
        print("Объект {set1} является чистым супермножеством")
    elif set2.issuperset(set1):
        print("Объект {set2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")
set1 = set(input("Введите элементы первого множества через пробел: ").split())
set2 = set(input("Введите элементы второго множества через пробел: ").split())
result4 = superset(set1,set2)
print(result4)

#Задание 5
def set_gen(numbers):
    count = {}
    result = set()
    for num in numbers:
        if num in count:
            count[num] += 1
            result.add(str(num) * count[num])
        else:
            count[num] = 1
            result.add(num)
    return result
numbers = input("Введите список натуральных чисел через пробел: ").split()
numbers = [int(x) for x in numbers]
result5 = set_gen(numbers)
print(result5)