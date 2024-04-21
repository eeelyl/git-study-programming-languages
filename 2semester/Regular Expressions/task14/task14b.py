def replace_case_insensitive(text, old_substring, new_substring):
    return re.sub(re.compile(re.escape(old_substring), re.IGNORECASE), new_substring, text)

# Пример использования:
text = "Hello, world!"
old_substring = "hello"
new_substring = "Hi"
result = replace_case_insensitive(text, old_substring, new_substring)
print("Результат замены:", result)
