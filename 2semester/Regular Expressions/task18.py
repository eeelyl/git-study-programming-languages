import re


def starts_and_ends_with_vowel(word):
    return re.match(r'^[aeiouAEIOU].*[aeiouAEIOU]$', word) is not None


# Пример использования:
test_cases = ["Red Orange White", "Red White Black", "abcd dkise eosksu"]
for test_case in test_cases:
    words = test_case.split()
    result = all(starts_and_ends_with_vowel(word) for word in words)
    print(f'("{test_case}") -> {result}')
