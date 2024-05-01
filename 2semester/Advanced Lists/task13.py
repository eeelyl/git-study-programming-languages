def custom_sort(list1, list2):
    # Создаем список кортежей, состоящих из элементов list1 и соответствующих им значений из list2
    combined = zip(list1, list2)
    # Сортируем кортежи по значениям из list2
    sorted_combined = sorted(combined, key=lambda x: x[1])
    # Возвращаем только элементы из первого списка после сортировки
    return [x[0] for x in sorted_combined]


# Примеры использования
list1_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2_1 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print(custom_sort(list1_1, list2_1))

list1_2 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
list2_2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print(custom_sort(list1_2, list2_2))
