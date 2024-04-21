import re

def remove_lowercase_substrings(text):
    return re.sub(r'\b[a-z]+\b', '', text)

# Пример использования:
text = "This is a Test string with some lowercase words"
cleaned_text = remove_lowercase_substrings(text)
print("Строка без подстрок нижнего регистра:", cleaned_text)
