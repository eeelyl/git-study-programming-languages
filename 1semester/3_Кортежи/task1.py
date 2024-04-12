# Напишите функцию tpl_sort(), которая сортирует кортеж, состоит из целых чисел по возрастанию и возвращает его.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.


def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


print(tpl_sort(-5, 245, 16, 1661, 2))
print(tpl_sort((-5, 245, 16, 1661, 2, 0.1)))
