import re


def replace_spaces_and_underscores(text):
    result = re.sub(r'(\s+)', '_', text)
    result = re.sub(r'(_+)', ' ', result)
    return result


# Пример использования:
text = "This is a sample_text."
result = replace_spaces_and_underscores(text)
print("Результат замены пробелов и подчеркиваний:", result)
