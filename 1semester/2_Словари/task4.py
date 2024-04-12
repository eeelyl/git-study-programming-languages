# Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта. Удалите второй элемент.
# Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).


dict = {1: 'first', 2: 'second', 3: 'third',
        4: 'forth', 5: 'fifth', 6: 'sixth'}
keys = list(dict.keys())
values = list(dict.values())

dict[keys[0]] = values[-1]
dict[keys[-1]] = values[0]
del dict[keys[1]]
dict['new_key'] = 'new_value'
print(dict)