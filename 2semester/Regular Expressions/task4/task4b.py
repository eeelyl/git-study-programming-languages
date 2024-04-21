import re


def check_digit_at_end(input_string, digit):
    pattern = rf'{digit}$'
    if re.search(pattern, input_string):
        return True
    else:
        return False


# Пример использования:
input_string = "Hello world 123"
digit = "3"
print(check_digit_at_end(input_string, digit))  # Выведет: True

input_string = "Hello 456"
digit = "7"
print(check_digit_at_end(input_string, digit))  # Выведет: False
