import re


def to_snake_case(text):
    return re.sub(r'\W+', '_', text).lower()


# Пример использования:
text = "btw... -what- * -do * -you-call-that-naming-style? -snake-case?"
snake_string = to_snake_case(text)
print("Snake-case строка:", snake_string)
