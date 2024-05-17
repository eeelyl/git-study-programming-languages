def transform_text(upper_func, lower_func, message):
    upper_message = upper_func(message)
    lower_message = lower_func(message)
    return upper_message, lower_message


def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


# Пример использования
message = "РегистР Преобразован функцией, полученной в качестве аргумента"
upper_message, lower_message = transform_text(to_upper, to_lower, message)

print(upper_message)
print(lower_message)
