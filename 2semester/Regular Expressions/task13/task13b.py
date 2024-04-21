import re


def find_adverbs(text):
    pattern = r'\b\w+ly\b'
    adverbs_with_positions = [(match.group(), match.start())
                              for match in re.finditer(pattern, text)]
    return adverbs_with_positions


# Пример использования:
sentence = "Clearly, he has no hardly excuse for such behavior."
adverbs = find_adverbs(sentence)
print("Найденные английские наречия и их позиции:", adverbs)
