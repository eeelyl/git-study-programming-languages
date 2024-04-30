import re


def snake_to_camel_case(snake_case):
    camel_case = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)
    return camel_case


# Пример использования
snake_string = "btw_what_do_you_call_that_naming_style"
camel_string = snake_to_camel_case(snake_string)
print(camel_string)
