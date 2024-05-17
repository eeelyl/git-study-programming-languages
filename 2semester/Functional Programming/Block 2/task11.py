def decorator_func(func):
    def wrapper(*args, **kwargs):
        pos_args_count = len(args)
        kw_args_count = len(kwargs)
        print(
            f"Функция получила позиционных аргументов: {pos_args_count}, именованных аргументов: {kw_args_count}")
        return func(*args, **kwargs)
    return wrapper


@decorator_func
def names_and_age(age1, age2, age3, name1, name2, name3):
    return f'У меня есть три сестры: {name1}, ей {age1} лет; {name2}, ей {age2} лет; {name3} - ей {age3} лет\n'


@decorator_func
def position_and_salary(sal1, sal2, sal3, sal4, pos1, pos2, pos3, pos4):
    return f'{pos1} получает {sal1} тыс, {pos2} получает {sal2} тыс, {pos3} получает {sal3} тыс, {pos4} получает {sal4} тыс\n'


# Пример вызова 1
print(names_and_age(12, 15, 13, name1='Света', name2='Маша', name3='Ира'))

# Пример вызова 2
print(position_and_salary(320, 150, 230, 170, pos1='разработчик',
      pos2='тестировщик', pos3='девопс', pos4='сисадмин'))
