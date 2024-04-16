# Задан список:
# flst = [[1,2,3],[8,9,12,17],[3,7]] 
# Сформируйте из элементов всех подсписков одномерный упорядоченный список
# [1, 2, 3, 3, 7, 8, 9, 12, 17] и выведите его на печать.
# Есть решение в одну строку.

def flatten_recursive(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_recursive(item))
        else:
            flat_list.append(item)
    return flat_list

flst = [[1,2,3],[8,9,12,17],[3,7]]
flat_sorted_list = sorted(flatten_recursive(flst))
print(flat_sorted_list)
        