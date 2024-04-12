# На основании 3 исходных множеств (передаются в качестве аргументов функции diff()) требуется написать функцию, которая будет возвращать либо симметричную разность,
# либо просто разность (если дополнительный аргумент функции symmetric имеет значение False) приведенных объектов в порядке: 1-ое множество, 2-ое множество, 3-е множество.
def diff(set1, set2, set3, symmetric=True):
    if symmetric:
        result = set1.symmetric_difference(set2).symmetric_difference(set3)
    else:
        result = set1.difference(set2).difference(set3)
    return result


set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
set2 = set([2, 3, 6])
set3 = set([2, 3, 7, 8])
print("Симметричная разность: ", diff(set1, set2, set3))
print("Простая разность: ", diff(set1, set2, set3, symmetric=False))
