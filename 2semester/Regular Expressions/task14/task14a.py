import re


def split_by_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)


# Пример использования:
text = "SplitThisStringByUppercaseLetters"
substrings = split_by_uppercase(text)
print("Подстроки, разделенные по прописным буквам:", substrings)
