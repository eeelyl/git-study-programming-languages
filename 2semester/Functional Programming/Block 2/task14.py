# Исходные данные
data = [{'name': 'wonderful sunset on the volga', 'country': 'UK', 'active_state': False},
        {'name': 'fantastic sunrise in .crimea. ',
            'country': 'Germany', 'active_state': False},
        {'name': 'good rain in Vladivostok.', 'country': 'Spain', 'active_state': True}]


def set_new_country(band):
    """Устанавливает страну 'Russia'."""
    band['country'] = 'Russia'
    return band


def correct_name(band):
    """Корректирует имя: убирает точки и приводит к заглавным буквам."""
    band['name'] = band['name'].replace('.', '').title()
    return band


def toggle_active_state(band):
    """Переключает булевское значение 'active_state'."""
    band['active_state'] = not band['active_state']
    return band


def pipeline(data, functions):
    """Применяет функции преобразования ко всем элементам данных."""
    for func in functions:
        data = [func(band) for band in data]
    return data


# Список функций преобразования
functions = [set_new_country, correct_name, toggle_active_state]

# Применение конвейера к данным
transformed_data = pipeline(data, functions)

# Вывод результата
print(transformed_data)
