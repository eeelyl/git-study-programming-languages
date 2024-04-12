# Перед студентом стоит задача: на вход функции sieve() поступает список целых чисел.
# В результате выполнения этой функции будет получен кортеж уникальных элементов списка в обратном порядке.

def sieve(lst):
    unique = []
    [unique.append(item) for item in reversed(lst) if item not in unique]
    return tuple(unique)



lst = [1, 2, 2, 2, 23, 24, 3, 5, 6, 5, 6, 8, 7]
print(sieve(lst))
