def find_substring(text, substring):
    positions = []
    index = text.find(substring)
    while index != -1:
        positions.append(index)
        index = text.find(substring, index + 1)
    return positions

# Пример использования:
text = "This is a sample text with sample substring."
substring = "sample"
positions = find_substring(text, substring)
if positions:
    print(f"Подстрока '{substring}' найдена в позициях:", positions)
else:
    print(f"Подстрока '{substring}' не найдена в тексте.")
