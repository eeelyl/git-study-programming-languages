def is_palindrome(s):
    # Удаляем из строки все символы, кроме букв, и приводим к нижнему регистру
    s = ''.join(filter(str.isalpha, s.lower()))

    # Базовый случай: если строка состоит из одного символа или пустая, то это палиндром
    if len(s) <= 1:
        return True
    # Рекурсивный случай: сравниваем первый и последний символы строки и вызываем функцию для оставшейся части
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Пример использования
user_input = input("Введите строку: ")
print(is_palindrome(user_input))
