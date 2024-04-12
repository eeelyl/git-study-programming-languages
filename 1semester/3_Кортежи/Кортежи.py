#Задание 1
def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):  #проверяет, является ли элемент целым числом
            return tpl  #если не является, то возвращает исходный кортеж
    return tuple(sorted(tpl)) #преобразование в отсортированный кортеж
print(tpl_sort((5, 2, 7, 1)))
print(tpl_sort((1.5,2,1,7)))

#Задание 2
def slicer(any_tuple, element):
    if element in any_tuple:
        if any_tuple.count(element) > 1:
            first_index = any_tuple.index(element)  #индекс первого вхождения данного элемента
            second_index = any_tuple.index(element, first_index + 1) + 1 #индекс последнего вхождения данного элемента
            return any_tuple[first_index:second_index]  #возвращаем кортеж, который является срезом вхождения элементов 
        else:
            return any_tuple[any_tuple.index(element):]  #если элемент входит один раз, то возвращаем срез с него и до конца кортежа
    else:
        return ()
task2_input = input("Введите элементы кортежа через запятую: ")
elements = task2_input.split(",")
tuple_elements = tuple(elements)
random_element = input("Введите случайный элемент: ")
result2 = slicer(tuple_elements,random_element)
print(result2)

#Задание 3
def sieve(lst):
    unique = []
    [unique.append(item) for item in reversed(lst) if item not in unique] #добавляем элемент в список, если он уникальный (смотрим по списку, который развернули)
    return tuple(unique)
lst = input("Введите элементы списка через пробел: ").split()
lst = [int(x) for x in lst]
result3 = sieve(lst)
print(result3)

#Задание 4
def del_from_tuple(tpl, elem):
    lst = list(tpl)
    if elem in tpl:
        lst.remove(elem)
    return tuple(lst)
task4_input = input("Введите элементы кортежа через запятую: ")
elements = task4_input.split(",")
tuple_elements = tuple(elements)
special_element = input("Введите элемент, первое вхождение которого будет удалено: ")
result4 = del_from_tuple(tuple_elements,special_element)
print(result4)

#Задание 5
from collections import namedtuple
Student = namedtuple('Student', 'name age mark city')  #создаем объект с 4 обозначаемыми полями
students = (
   Student('Злата', '18', 5, 'Саратов'),
   Student('Мария', '18', 5, 'Казань'),
   Student('Елена', '19', 4, 'Москва'),
   Student('Анна', '21', 4, 'Нижний Новгород'),
   Student('Кирилл', '20', 3, 'Самара'),
   Student('Николай', '22', 2, 'Владивосток'),
   Student('Дмитрий', '20', 3, 'Екатеринбург')
)
def good_students(students):
   total_mark = 0
   for student in students:
       total_mark += student.mark
   avg_mark = total_mark / len(students)  #средняя оценка по всем учащимся
   good_mark_students = [student.name for student in students if student.mark >= avg_mark]
   print('Ученики ', ', '.join(good_mark_students), ' в этом семестре хорошо учатся!')
good_students(students)