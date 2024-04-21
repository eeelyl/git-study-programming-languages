import re


def find_numbers(text):
    numbers = re.findall(r'\b\d+\b', text)
    positions = [match.start() for match in re.finditer(r'\b\d+\b', text)]
    return numbers, positions


# Пример использования:
text = "There are 123 apples and 456 oranges in the basket."
numbers, positions = find_numbers(text)
print("Найденные числа:", numbers)
print("Их положение:", positions)
