def split_by_multiple_delimiters(text, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(pattern, text)


# Пример использования:
text = "Split,this-string.by:various_delimiters"
delimiters = [',', '-', '.', ':', '_']
substrings = split_by_multiple_delimiters(text, delimiters)
print("Подстроки, разделенные по различным разделителям:", substrings)
