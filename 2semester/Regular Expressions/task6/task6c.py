import re

def extract_numbers(text):
    pattern = r'\b\d+\b'
    numbers = re.findall(pattern, text)
    return numbers

# Пример использования:
text = 'There are 123 apples and 456 oranges in the basket.'
numbers = extract_numbers(text)
print("Найденные числа:", numbers)
