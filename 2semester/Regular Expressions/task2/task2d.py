import re


def match_pattern_d(input_string):
    pattern = r'ab{3}'
    if re.match(pattern, input_string):
        return True
    else:
        return False


# Пример использования:
input_string = "abbb"
print(match_pattern_d(input_string))  # Выведет: True

input_string = "abbbb"
print(match_pattern_d(input_string))  # Выведет: False
