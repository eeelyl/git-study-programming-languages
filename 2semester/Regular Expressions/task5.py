import re


def find_substrings(text, substrings):
    found = {}
    for substring in substrings:
        pattern = re.compile(r'\b' + re.escape(substring) + r'\b')
        match = re.search(pattern, text)
        found[substring] = match is not None
    return found


# Пример использования:
text = "Fast brown fox leaps over lazy dog"
substrings = ['fox', 'dog', 'horse']
results = find_substrings(text, substrings)
for substring, found in results.items():
    if found:
        print(f"'{substring}' найдено в тексте.")
    else:
        print(f"'{substring}' не найдено в тексте.")
