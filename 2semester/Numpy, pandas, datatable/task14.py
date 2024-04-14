import datatable as dt

# Заданные объекты datatable.Frame
df1 = dt.Frame(A=[1, 2, 3, 4], B=['a', 'b', 'c', 'd'])
df2 = dt.Frame(A=[1, 2, 3, 4, 5], C=['a2', 'b2', 'c2', 'd2', 'e2'])

# Выполняем left join по ключу A
merged_df = df1[:, :, dt.join(df2)]

print("Результат left join:")
print(merged_df)
