import re

def camel_to_snake_case(text):
    # Добавляем пробел перед каждой заглавной буквой, кроме первой
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    # Заменяем пробелы и заглавные буквы на подчеркивания и строчные буквы
    text = re.sub(r'[^a-zA-Z0-9]+', '_', text).lower()
    return text

# Пример использования:
text = "btw... -what- * -do * -you-call-that-naming-style? -snake-case?"
snake_case_text = camel_to_snake_case(text)
print("Результат преобразования в snake-case:", snake_case_text)
