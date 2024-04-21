import re

def find_five_letter_words(text):
    words = re.findall(r'\b\w{5}\b', text)
    return words

# Пример использования:
text = "This is a sample text with some five-letter words like apple and mango."
five_letter_words = find_five_letter_words(text)
print("Найденные пятисимвольные слова:", five_letter_words)
