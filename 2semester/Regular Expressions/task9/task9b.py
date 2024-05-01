def convert_date_format(date):
    parts = date.split('-')
    if len(parts) == 3:
        return f"{parts[2]}-{parts[1]}-{parts[0]}"
    else:
        return None


# Пример использования:
date = "2016-09-02"
converted_date = convert_date_format(date)
print("Преобразованная дата:", converted_date)
