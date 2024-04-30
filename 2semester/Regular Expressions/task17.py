import re


def merge_consecutive_numbers(text):
    return re.sub(r'(\b\d+)\s+(\d+\b)', r'\1\2', text)


# Пример использования:
text = "Введите на 1 20 Kearny Street. Служба безопасности может направить вас на этаж 1 6. Пожалуйста, подготовьте удостоверение личности."
result = merge_consecutive_numbers(text)
print("После объединения последовательных чисел:", result)
