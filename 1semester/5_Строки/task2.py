# Требуется определить индексы первого и последнего вхождения буквы в строке.
# Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра: letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть,
# то кортеж будет состоять из первого и последнего индекса этого символа.

def first_last(letter, st):
    first_index = st.lower().find(letter.lower())
    last_index = st.lower().rfind(letter.lower())
    if first_index == -1:
        return (None, None)
    else:
        return (first_index, last_index)


letter = input("Введите искомую букву: ")
string = input("Введите строку: ")
print(first_last(letter, string))
