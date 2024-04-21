import re


def find_uppercase_lowercase_sequences(input_string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, input_string)
    return sequences


# Пример использования:
input_string = "HelloWorld isATest"
print(find_uppercase_lowercase_sequences(input_string))
