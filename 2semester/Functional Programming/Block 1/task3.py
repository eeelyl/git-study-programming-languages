from functools import reduce

# Функция, вычисляющая среднее значение роста


def calculate_average_height(people):
    # Фильтрация людей с указанным ростом
    heights = list(filter(lambda person: 'рост' in person, people))
    # Получение только значений роста
    heights_values = map(lambda person: person['рост'], heights)
    # Вычисление суммы роста
    height_total = reduce(lambda x, y: x + y, heights_values, 0)
    # Вычисление количества людей с указанным ростом
    height_count = len(heights)
    # Вычисление среднего значения роста
    if height_count > 0:
        average_height = height_total / height_count
        print(average_height)
    else:
        print("Нет данных о росте")


# Пример данных
people = [
    {'имя': 'Иван', 'возраст': 25, 'рост': 180},
    {'имя': 'Мария', 'возраст': 30},
    {'имя': 'Петр', 'возраст': 35, 'рост': 175},
    {'имя': 'Анна', 'возраст': 40, 'рост': 165}
]

# Вызов функции для вычисления среднего значения роста
calculate_average_height(people)
