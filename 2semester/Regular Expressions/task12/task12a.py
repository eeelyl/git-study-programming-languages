import re


def remove_extra_spaces(text):
    return re.sub(r'\s+', ' ', text)


# Пример использования:
text = "This     is    a    sentence     with    extra   spaces."
cleaned_text = remove_extra_spaces(text)
print("Строка без множественных пробелов:", cleaned_text)
