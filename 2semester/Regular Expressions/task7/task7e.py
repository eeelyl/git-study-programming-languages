import re


def find_words_at_least_four_chars(text):
    words = re.findall(r'\b\w{4,}\b', text)
    return words


# Пример использования:
text = "There are some words with different lengths, such as apple, banana, and orange."
words = find_words_at_least_four_chars(text)
print("Найденные слова:", words)
