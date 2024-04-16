# Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.

arr = input('Введите список: ').split()
def list_sort(lst):
    return sorted(lst, key = lambda x: abs(int(x)), reverse = True)
print('Измененный список: ', list_sort(arr))
