def snake_to_camel_case(text):
    # Разбиваем строку по подчеркиваниям, преобразуем первую букву каждого слова в заглавную
    words = [word.capitalize() for word in text.split('_')]
    # Объединяем слова и убираем пробелы
    camel_case_text = ''.join(words)
    return camel_case_text


# Пример использования:
text = "btw... -what- * -do * -you-call-that-naming-style? -snake-case?"
camel_case_text = snake_to_camel_case(text)
print("Результат преобразования в camel-case:", camel_case_text)
