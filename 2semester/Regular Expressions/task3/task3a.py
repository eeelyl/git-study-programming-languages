import re


def extract_word_at_beginning(input_string):
    pattern = r'^\w+'
    match = re.match(pattern, input_string)
    if match:
        return match.group()
    else:
        return None


# Пример использования:
input_string = "Hello world"
print(extract_word_at_beginning(input_string))  # Выведет: Hello

input_string = "123 hello world"
print(extract_word_at_beginning(input_string))  # Выведет: 123
