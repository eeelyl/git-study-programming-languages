import re

def remove_non_alphanumeric(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text)

# Пример использования:
text = "This is a sentence with 123 and special characters !@#"
cleaned_text = remove_non_alphanumeric(text)
print("Строка без специальных символов:", cleaned_text)
