#Задание 1
def search_substr(subst, st):
    if st.lower().find(subst.lower()) != -1: #если подстрока subst содержится в строке sub (преобразуем все в нижний регистр)
        return "Есть контакт!"
    else:
        return "Мимо!"
substring = input("Введите первую строку: ")
string = input("Введите вторую строку: ")
result1 = search_substr(substring, string)
print(result1)

#Задание 2
def first_last(letter, st):
    first_index = st.lower().find(letter.lower())  #индекс первого вхождения (все приводим к нижнему регистру)
    last_index = st.lower().rfind(letter.lower())  #индекс последнего вхождения (нижний регистр)
    if first_index == -1: #если вхождения найдено не было
        return (None, None)
    else:
        return (first_index, last_index)
letter = input("Введите искомую букву: ")
string = input("Введите строку: ")
result2 = first_last(letter, string)
print(result2)

#Задание 3
from collections import Counter 
def top3(st):
    st = st.replace(" ", "") #удаляем пробелы
    char_count = Counter(st)
    top_3 = char_count.most_common(3) #3 самые часто встречающиеся 
    result = ""
    for char, count in top_3:
        result += f"{char} - {count} раз, " #формируем ответ 
    result = result[:-2]
    return result 
text3 = input("Введите текст: ")
print(top3(text3))

#Задание 4
def camel(st):
    result = ""
    is_upper = True  #флаг для определения, нужно ли использовать заглавные буквы
    for char in st:
        if char.isalpha():  #проверяем, является ли символ буквой
            if is_upper:
                result += char.upper()  #с заглавной буквы
            else:
                result += char.lower()  #с маленькой буквы        
            is_upper = not is_upper  #инвертируем флаг для следующего символа (меняем значение на противоположное) 
        else:
            result += char  # Добавляем пробелы и знаки препинания без изменений
    return result
text4 = input("Введите текст: ")
print(camel(text4))

#Задание 5 (самая последняя скобка будет иметь после себя обязательно после себя закрывающую 
def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')  #возвращает индекс последнего вхождения данной строки
        right = st.find(')', left) #начинаем искать закрывающуюся скобку с индекса left 
        st = st.replace(st[left:right + 1], '') #делаем срез 
    return st
text5 = input("Введите текст: ")
print(shortener(text5))

#Задание 6
def cleaned_str(st):
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop() #удаляем
        elif symbol != '@':
            clean_lst.append(symbol) #добавляем 
    return ''.join(clean_lst)
text6 = input("Введите строку: ")
print(cleaned_str(text6))