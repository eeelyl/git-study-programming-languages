#Задание 1
def more_than_five(lst):
    new_lst = []
    for num in lst:
        if abs(int(num)) > 5:
            new_lst.append(num)
    return new_lst
lst = input("Введите элементы списка через пробел: ").split()
print(more_than_five(lst))

#Задание 2
letters = input("Введите исходную строку: ")
clean_string = ''
for letter in letters:
    if not letter.isupper(): #если символ не будет записан в верхнем регистре
        clean_string += letter  #то добавляем к пустой строк нашу букву
letters = clean_string
print(letters)

#Задание 3
rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for position in range(11):
    print('^' * 27)
    for letter in rus_lower:
        if rus_lower.index(letter) % 11 == position:
            print('| ', letter.upper(), letter, ' |', end='')
    print()
print('^' * 27)

#Задание 4
nick = input()
secret_list = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']
while nick not in secret_list:
    print('Тут ничего нет. Еще есть вопросы?')
    nick = input('Введите свой ник: ')
else:
	print(f'Ты – свой. Приветствую, любезный {nick}!')

#Задание 5
def all_divisors(number):
    lst = [1, number] #преовначально в наш список входит единица и само число
    for i in range(2, int(number**0.5) + 1): #перебираем до квадратного корня
        if number % i == 0:
            lst.extend({number // i, number}) #добавляет элементы, удовлятворяющие условию, в конец списка (итерируемый объект) 
    return sorted(lst)
print(all_divisors(23_436))
print(all_divisors(190_187_200))
print(all_divisors(380_457_890_232))
