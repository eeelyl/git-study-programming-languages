# TODO
# Решить без asyncio

# Исходные данные
data = [{'name': 'wonderful sunset on the volga', 'country': 'UK', 'active_state': False},
        {'name': 'fantastic sunrise in .crimea. ',
            'country': 'Germany', 'active_state': False},
        {'name': 'good rain in Vladivostok.', 'country': 'Spain', 'active_state': True}]

# Функция для установки новой страны


def set_new_country(band):
    band['country'] = 'Russia'
    return band

# Функция для исправления имени


def correct_name(band):
    band['name'] = band['name'].replace('.', '').title()
    return band

# Функция для переключения активного состояния


def toggle_active_state(band):
    band['active_state'] = not band['active_state']
    return band

# Функция pipeline для обработки данных


def pipeline(data, *functions):
    for func in functions:
        data = list(map(func, data))
    return data

# Основная функция для запуска pipeline


def main(data):
    return pipeline(data, set_new_country, correct_name, toggle_active_state)


# Запуск основного конвейера
data = main(data)

# Вывод результата
print(data)
