import re

def remove_text_in_parentheses(text):
    return re.sub(r'\s*\([^()]*\)', '', text)

# Пример использования:
text = "example (.com) w3resource github (.com) stackoverflow (.com)"
result = remove_text_in_parentheses(text)
print("Результат:", result)
