import datatable as dt
import pandas as pd

# Загружаем датасет в формате datatable.Frame
url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
df_dt = dt.fread(url)

# Преобразуем в формат Pandas DataFrame
df_pd = df_dt.to_pandas()

# Преобразуем в формат NumPy array
arr_np = df_dt.to_numpy()

# Преобразуем в формат словаря
dict_data = df_dt.to_dict()

# Преобразуем в формат списка (list)
list_data = df_dt.to_list()

# Преобразуем в формат кортежа (tuple)
tuple_data = df_dt.to_tuples()

# Выводим результаты
print("Pandas DataFrame:")
print(df_pd.head())

print("\nNumPy array:")
print(arr_np[:5])

print("\nСловарь:")
print(dict_data)

print("\nСписок:")
print(list_data[:5])

print("\nКортеж:")
print(tuple_data[:5])
