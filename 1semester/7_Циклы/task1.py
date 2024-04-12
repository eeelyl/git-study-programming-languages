# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.

def more_than_five(lst):
    new_lst = []
    for num in lst:
        if abs(int(num)) > 5:
            new_lst.append(num)
    return new_lst


lst = input("Введите элементы списка через пробел: ").split()
print(more_than_five(lst))
