import re

def convert_date_format(date):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)

# Пример использования:
date = "2016-09-02"
converted_date = convert_date_format(date)
print("Преобразованная дата:", converted_date)
