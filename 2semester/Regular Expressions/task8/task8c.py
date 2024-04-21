import re


def replace_spaces_commas_dots_with_colon(text):
    result = re.sub(r'[ ,.]', ':', text)
    return result


# Пример использования:
text = "This is a sample, text. With spaces and commas."
result = replace_spaces_commas_dots_with_colon(text)
print("Результат замены пробелов, запятых и точек на двоеточия:", result)
