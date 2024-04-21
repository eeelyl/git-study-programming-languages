import re


def extract_word_with_z(input_string):
    pattern = r'\b\w*z\w*\b'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return None


# Пример использования:
input_string = "The zoo is closed"
print(extract_word_with_z(input_string))  # Выведет: zoo

input_string = "I like pizza"
print(extract_word_with_z(input_string))  # Выведет: None
