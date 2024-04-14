import datatable as dt

# Загружаем датасет
url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
df = dt.fread(url)

# Получаем типы данных всех столбцов
column_types = df.stypes

# Выводим типы данных всех столбцов
for col, col_type in column_types.items():
    print(f"{col} : {col_type}")
