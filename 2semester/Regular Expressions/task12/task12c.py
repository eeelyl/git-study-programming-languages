import re


def remove_words_by_length(text, length):
    return re.sub(r'\b\w{1,' + str(length) + r'}\b', '', text)


# Пример использования:
text = "This is a sentence with some short and long words"
length = 4
cleaned_text = remove_words_by_length(text, length)
print(f"Строка без слов длиной от 1 до {length} символов:", cleaned_text)
