import re


def find_urls(text):
    pattern = r'\b(?:https?://|www\.)\S+\b'
    urls = re.findall(pattern, text)
    return urls


# Пример использования:
text = "Visit my website at https://www.example.com or check out https://github.com"
urls = find_urls(text)
print("Найденные URL-адреса:", urls)
