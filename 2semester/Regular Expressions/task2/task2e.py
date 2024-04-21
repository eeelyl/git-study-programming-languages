import re

def match_pattern_e(input_string):
    pattern = r'.*b$'
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Пример использования:
input_string = "somethingb"
print(match_pattern_e(input_string))  # Выведет: True

input_string = "anotherthing"
print(match_pattern_e(input_string))  # Выведет: False
