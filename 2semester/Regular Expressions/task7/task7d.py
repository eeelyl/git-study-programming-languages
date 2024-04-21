import re


def find_words_of_lengths(text, lengths):
    words = re.findall(r'\b\w{%s}\b' % '|'.join(map(str, lengths)), text)
    return words


# Пример использования:
text = "There are some short words like cat, dog, and bird."
lengths = [3, 4, 5]
words = find_words_of_lengths(text, lengths)
print("Найденные слова:", words)
