# Функция slicer() на вход принимает кортеж и случайный элемент.
# Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.


def slicer(tpl, element):
    if element in tpl:
        if tpl.count(element) > 1:
            first_index = tpl.index(element)
            second_index = tpl.index(element, first_index + 1) + 1
            return tpl[first_index:second_index]
        else:
            return tpl[tpl.index(element):]
    else:
        return ()


elements = ('1', '2', '3', '4', '5', '6', '2', '7', '2')
any_elem = input("Введите любой элемент: ")
result = slicer(elements, any_elem)
print(result)
