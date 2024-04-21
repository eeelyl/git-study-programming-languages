import re


def shorten_road(text):
    result = re.sub(r'\b(Road)\b', 'Rd.', text)
    return result


# Пример использования:
text = "123 Main Road"
result = shorten_road(text)
print("Сокращенная версия строки:", result)
