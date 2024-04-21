import re

def find_words_starting_with_a_or_e(text):
    words = re.findall(r'\b[ae]\w+', text, flags=re.IGNORECASE)
    return words

# Пример использования:
text = "An apple is on the table, while an elephant is in the room."
words = find_words_starting_with_a_or_e(text)
print("Слова, начинающиеся с 'a' или 'e':", words)
