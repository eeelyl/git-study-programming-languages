import re


def check_string(input_string):
    pattern = r'^[a-zA-Z0-9]+$'
    if re.match(pattern, input_string):
        return True
    else:
        return False


# Пример использования:
input_string = "abcDEF123"
print(check_string(input_string))

input_string = "abc!@#123"
print(check_string(input_string))
