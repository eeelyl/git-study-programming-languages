import re

def insert_spaces_before_capitalized_words(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# Пример использования:
text = "ThisIsACamelCaseString"
result = insert_spaces_before_capitalized_words(text)
print("Результат с вставленными пробелами:", result)
