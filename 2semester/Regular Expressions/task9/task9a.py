import re

def extract_date_from_url(url):
    pattern = r'/(\d{4})/(\d{2})/(\d{2})/'
    match = re.search(pattern, url)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        return year, month, day
    else:
        return None, None, None

# Пример использования:
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
year, month, day = extract_date_from_url(url)
print("Год:", year)
print("Месяц:", month)
print("День:", day)
