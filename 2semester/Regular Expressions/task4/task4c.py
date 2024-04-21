import re


def find_numbers(input_string):
    pattern = r'\b\d{1,3}\b'
    numbers = re.findall(pattern, input_string)
    return numbers


# Пример использования:
input_string = "There are 123 cats and 456 dogs in the house."
print(find_numbers(input_string))  # Выведет: ['123', '456']
