# Создайте кортеж из 7-ми именованных кортежей учащихся ВУЗов.
# В именованном кортеже будут присутствовать следующие поля: имя студента, возраст, оценка за семестр, город проживания.
# Функция good_students() будет принимать этот кортеж, вычислять среднюю оценку по всем учащимся
# и выводить на печать следующее сообщение: "Ученики {список имен студентов через запятую} в этом семестре хорошо учатся!".
# В список студентов, которые выводятся по результатам работы функции, попадут лишь те, у которых оценка за семестр равна или выше средней по всем учащимся

from collections import namedtuple
# создаем объект с 4 обозначаемыми полями
Student = namedtuple('Student', 'name age mark city')
students = (
    Student('Иван', '19', 5, 'Москва'),
    Student('Егор', '19', 5, 'Москва'),
    Student('Кристина', '19', 4, 'Москва'),
    Student('Кирилл', '21', 4, 'Саратов'),
    Student('Мефодий', '22', 3, 'Саратов'),
    Student('Александр', '18', 2, 'Саратов'),
    Student('Владимир', '18', 3, 'Сызрань')
)


def good_students(students):
    total_mark = 0
    for student in students:
        total_mark += student.mark
    avg_mark = total_mark / len(students)
    good_mark_students = [
        student.name for student in students if student.mark >= avg_mark]
    print('Ученики ', ', '.join(good_mark_students),
          ' в этом семестре хорошо учатся!')


good_students(students)
