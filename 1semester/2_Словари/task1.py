# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

def to_dict(lst):
    return {x: x for x in lst}


lst = input("Введите элементы списка через пробел: ").split()
result1 = to_dict(lst)
print(result1)
