from collections import Counter


def count_occurrences(lst, x):
    # Создаем объект Counter из списка
    counts = Counter(lst)
    # Возвращаем количество вхождений числа x
    return counts[x]


# Примеры входных данных
lst1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x1 = 10

lst2 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x2 = 16

# Вызываем функцию для каждого примера и выводим результаты
print("Output 1:", count_occurrences(lst1, x1))
print("Output 2:", count_occurrences(lst2, x2))
