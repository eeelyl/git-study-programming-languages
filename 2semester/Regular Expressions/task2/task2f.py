import re

def match_pattern_f(input_string):
    pattern = r'.*b{2,3}$'
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Пример использования:
input_string = "abb"
print(match_pattern_f(input_string))  # Выведет: True

input_string = "abbb"
print(match_pattern_f(input_string))  # Выведет: True

input_string = "abbbb"
print(match_pattern_f(input_string))  # Выведет: False
