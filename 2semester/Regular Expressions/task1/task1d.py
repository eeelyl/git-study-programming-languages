import re

def find_valid_strings(input_strings):
    pattern = r'^[a-zA-Z0-9_]+$'
    valid_strings = [s for s in input_strings if re.match(pattern, s)]
    return valid_strings

# Пример использования:
input_strings = ["abc_DEF123", "hello world", "GoodMorning", "test_123"]
print(find_valid_strings(input_strings))  # Выведет: ['abc_DEF123', 'GoodMorning', 'test_123']
