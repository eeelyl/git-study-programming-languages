import re

def extract_word_at_end(input_string):
    pattern = r'\b\w+\b[.,;:]*$'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return None

# Пример использования:
input_string = "Hello world."
print(extract_word_at_end(input_string))  # Выведет: world

input_string = "Hello world,"
print(extract_word_at_end(input_string))  # Выведет: world
