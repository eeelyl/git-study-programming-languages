import re

def find_lowercase_sequences(input_string):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, input_string)
    return sequences

# Пример использования:
input_string = "hello_world is_a_test"
print(find_lowercase_sequences(input_string))  # Выведет: ['hello_world', 'is_a']
