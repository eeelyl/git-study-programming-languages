import re


def two_words_start_with_P(words):
    p_words = [word for word in words if re.match(r'^P', word)]
    return len(p_words) >= 2


# Пример использования:
word_list = ['Python', 'Perl', 'Java', 'PHP', 'C++']
if two_words_start_with_P(word_list):
    print("Два слова из списка начинаются с буквы 'P'.")
else:
    print("Меньше двух слов из списка начинаются с буквы 'P'.")
