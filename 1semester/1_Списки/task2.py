# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент. 
# В исходном списке минимум 2 элемента.

arr = input('Введите список: ').split()
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
changed_arr = change(arr)
print('Измененный список: ', changed_arr)