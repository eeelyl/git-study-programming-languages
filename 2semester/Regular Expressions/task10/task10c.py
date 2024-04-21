import re

def is_decimal_with_two_decimal_places(string):
    pattern = r'^\d+(\.\d{1,2})?$'
    return bool(re.match(pattern, string))

# Пример использования:
number1 = "123.45"
number2 = "3.14159"
number3 = "42"
print(f"{number1}: {is_decimal_with_two_decimal_places(number1)}")
print(f"{number2}: {is_decimal_with_two_decimal_places(number2)}")
print(f"{number3}: {is_decimal_with_two_decimal_places(number3)}")
