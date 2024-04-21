import re

def match_pattern_b(input_string):
    pattern = r'ab+'
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Пример использования:
input_string = "ab"
print(match_pattern_b(input_string))  # Выведет: True

input_string = "abb"
print(match_pattern_b(input_string))  # Выведет: True

input_string = "ac"
print(match_pattern_b(input_string))  # Выведет: False
