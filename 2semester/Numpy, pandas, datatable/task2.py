import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1, 100, 16).reshape(4, 4),
                  columns=list('efgh'), index=list('abcd'))

print("Исходный DataFrame:")
print(df)

# Вычисляем корреляционную матрицу
corr_matrix = df.corr().abs()

# Исключаем единичную диагональ, чтобы избежать корреляции с самим собой
np.fill_diagonal(corr_matrix.values, np.nan)

# Находим максимальное значение корреляции для каждого столбца
max_correlations = corr_matrix.max()

# Выводим максимальные значения корреляции
print("Максимальные значения абсолютной корреляции для каждого столбца:")
print(max_correlations)
