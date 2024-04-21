import re


def extract_strings_between_quotes(text):
    pattern = r'"(.*?)"'
    matches = re.findall(pattern, text)
    return matches


# Пример использования:
text = 'This is a "sample" text with "quoted" strings.'
extracted_strings = extract_strings_between_quotes(text)
print("Значения между кавычками:", extracted_strings)
