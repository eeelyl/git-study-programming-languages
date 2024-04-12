#Задание 1
def is_alive(health):
    if health <= 0:
        return False
    else:
        return True
health1 = int(input())
print(is_alive(health1))

#Задание 2
def season_events(number_of_month):
   months = {1: 'январе', 2: 'феврале', 3: 'марте', 4: 'апреле', 5: 'мае', 6: 'июне', 7: 'июле', 8: 'августе', 9: 'сентябре', 10: 'октябре', 11: 'ноябре', 12: 'декабре'}
   if 1 <= int(number_of_month) <= 12:
       if number_of_month in range(3, 6):
            print(f'Вы родились в {months[int(number_of_month)]}. Птицы пели прекрасные песни')
       elif number_of_month in range(6, 9):
            print(f'Вы родились в {months[int(number_of_month)]}. Солнце светило ярче чем когда-либо')
       elif number_of_month in range(9, 12):
            print(f'Вы родились в {months[int(number_of_month)]}. Урожай был невероятным')
       else:
           print(f'Вы родились в {months[int(number_of_month)]}. За окном падал белый снег')
   else:
       print('Требуется ввести реальный номер месяца')
number_of_month = input('Введите месяц вашего рождения: ')
print(season_events(number_of_month))


#Задание 3
import string
def check_pass(pwd):
    err = {  #ошибки в виде словаря
    'length': 'Длина пароля не равна 8 символам',
    'upper': 'Отсутствуют заглавные буквы',
    'lower': 'Нет строчных букв в пароле',
    'digits': 'Нет цифр в пароле',
    'spec': 'Отсутствуют специальные знаки в пароле',
    'bad_symbols': 'В пароле использованы непредусмотренные символы'
    }
    if len(pwd) == 8: #смотрим длину пароля
        err.pop('length')  
    if pwd.lower() != pwd:  #смотрим нижний регистр
        err.pop('upper')  
    if pwd.upper() != pwd:  #смотрим верхний регистр
        err.pop('lower')
    if any(map(str.isdigit, pwd)): #смотрим, чтобы было число
        err.pop('digits')
    if ('*' in pwd) or ('-' in pwd) or ('#' in pwd):  #смотрим, что был специальный символ
        err.pop('spec')
    allowed_sym = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'  #разрешенные символы
    if (set(pwd) - set(allowed_sym)) == set():
        err.pop('bad_symbols')  #множество плохих символов
    if len(err) == 0:  #если нет ошибок
        print('Пароль идеален')
    else:
        print(*err.values(), sep = '; ') #печатаем ошибки 
pwd3 = input('Введите возможный пароль: ')
print(check_pass(pwd3))

#Задание 4
def is_divisible_by_6(number):
    if isinstance(number, int): #проверяем, является ли введенное значение числом
        if (number % 10) % 2 == 0 and sum(int(digit) for digit in str(number)) % 3 == 0:
            return f"Число {number} делится на 6"
        else:
            return f"Число {number} не делится на 6"
    else:
        return "Требуется ввести целое число"
number4 = int(input("Введите число: "))
print(is_divisible_by_6(number4))