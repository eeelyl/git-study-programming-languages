import re


def find_literal_string(text, pattern):
    matches = re.finditer(pattern, text)
    positions = []
    for match in matches:
        positions.append(match.start())
    return positions


# Пример использования:
text = 'The quick brown fox jumps over the lazy dog.'
pattern = 'fox'
positions = find_literal_string(text, pattern)
if positions:
    print(f"Искомая строка '{pattern}' найдена в позициях:", positions)
else:
    print(f"Искомая строка '{pattern}' не найдена в тексте.")
