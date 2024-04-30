import re

def snake_to_camel_case(string):
    # Используем регулярное выражение для поиска слов, разделенных символом подчеркивания
    words = re.split(r'_', string)
    # Каждое слово кроме первого, преобразуем первую букву в заглавную
    camel_case = ''.join([words[0]] + [word.capitalize() for word in words[1:]])
    return camel_case

# Пример использования
snake_string = "btw_what_do_you_call_that_naming_style"
camel_string = snake_to_camel_case(snake_string)
print(camel_string)
