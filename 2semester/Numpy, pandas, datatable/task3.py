import pandas as pd

# Создаем DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

# Нормализуем все столбцы путем вычитания среднего значения и деления на стандартное отклонение
normalized_df = (df - df.mean()) / df.std()

# Применяем мин-макс нормализацию
normalized_df = (normalized_df - normalized_df.min()) / (normalized_df.max() - normalized_df.min())

print("Нормализованный DataFrame:")
print(normalized_df)
