import numpy as np


def sort_with_list(list1, list2):
    # Преобразование списков в массивы NumPy
    list1_arr = np.array(list1)
    list2_arr = np.array(list2)
    # Создание индексов, которые будут отсортированы с учетом порядка второго списка
    sorted_indices = np.argsort(list2_arr)
    # Использование отсортированных индексов для сортировки первого списка
    sorted_list1 = list1_arr[sorted_indices]
    return sorted_list1.tolist()


# Примеры входных данных
list1_1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2_1 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

list1_2 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
list2_2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

# Вызываем функцию для каждого примера и выводим результаты
print("Output 1:", sort_with_list(list1_1, list2_1))
print("Output 2:", sort_with_list(list1_2, list2_2))
