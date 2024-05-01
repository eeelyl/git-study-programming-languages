import re

def starts_and_ends_with_vowel(string):
    # Паттерн для поиска слов, начинающихся и заканчивающихся гласной буквой
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*[aeiouAEIOU]?\b'
    # Поиск всех слов, соответствующих паттерну в строке
    matches = re.findall(pattern, string)
    # Проверка, есть ли совпадения
    if matches:
        return True
    else:
        return False

# Пример использования
test_strings = [
    "Red Orange White",
    "Red White Black",
    "abcd dkise eosksu"
]

for test_string in test_strings:
    result = starts_and_ends_with_vowel(test_string)
    print(f'("{test_string}") -> {result}')
