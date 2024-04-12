#Задание 1
def to_dict(lst):  #принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом, и значением
    return {x: x for x in lst}
lst = input("Введите элементы списка через пробел: ").split()
result1 = to_dict(lst)
print(result1)

#Задание 2
def count_it(sequence):
    count_dict = {}
    for num in sequence:
        if num.isdigit():
            num = int(num)
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
    sorted_dict = sorted(count_dict.items(), key = lambda x: x[1], reverse = True) #сортируем словарь по значениям в порядке убывания
    result_dict = {} #словарь для тех самых часто встречающихся 
    for i in range(3):
        if i < len(sorted_dict):
            result_dict[sorted_dict[i][0]] = sorted_dict[i][1]
    return result_dict
sequence = input("Введите последовательность чисел: ")
result2 = count_it(sequence)
print("Словарь из 3 самых часто встречающихся слов: ", result2)

#Задание 4
n = int(input("Введите количество элементов в словаре: "))
dict = {}
for i in range(n):
    key = input("Введите ключ: ")
    value = input("Введите значение: ")
    dict[key] = value
keys = list(dict.keys())
values = list(dict.values())
dict[keys[0]] = values[-1]  #меняем местами первый и последний элементы словаря (значения в паре)
dict[keys[-1]] = values[0]
del dict[keys[1]]  #удаляем второй элемент
dict['new_key'] = 'new_value'
print(dict)

#Задание 5
def max_dct(*dicts):
    result = {}
    for dct in dicts:
        for key, value in dct.items():  #рассматриваем пары ключ-значение
            if key in result:
                result[key] = max(result[key], value)
            else:
                result[key] = value
    return result
def sum_dct(*dicts):
    result = {}
    for dct in dicts:
        for key, value in dct.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result
dct1 = {"a": 2, "b": 6, "c": 5}
dct2 = {"a": 11, "c": 15, "d": 2}
dct3 = {"b": 7, "e": 1, "f": 15}
dct4 = {"k": 12, "c": 14}
max_dictionary = max_dct(dct1, dct2, dct3, dct4)
print("Максимальные значения:", max_dictionary)
sum_dictionary = sum_dct(dct1, dct2, dct3, dct4)
print("Суммы значений:", sum_dictionary)