import re

def replace_max_two_spaces_commas_dots_with_colon(text):
    result = re.sub(r'[ ,.](?=[ ,.])', ':', text, count=2)
    return result

# Пример использования:
text = "This is a sample, text. With multiple spaces, commas, and dots."
result = replace_max_two_spaces_commas_dots_with_colon(text)
print("Результат замены максимум 2 пробелов, запятых и точек на двоеточия:", result)
