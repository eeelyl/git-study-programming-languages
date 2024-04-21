import re

def is_valid_sequence(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    for i in range(len(words) - 1):
        if words[i][-1] in 'aeiouAEIOU' and words[i + 1][0] in 'aeiouAEIOU':
            return True
    return False

# Пример использования:
test_cases = [
    "These exercises can be used for practice.",
    "Following exercises should be removed for practice."
]
for test_case in test_cases:
    result = is_valid_sequence(test_case)
    print(f'("{test_case}") -> {result}')
