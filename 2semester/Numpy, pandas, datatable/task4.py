import pandas as pd
import numpy as np

# Создаем DataFrame
df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['low', 'medium', 'high'] * 3,
    'price': np.random.randint(0, 100, 9)
})

df2 = pd.DataFrame({
    'frukt': ['apple', 'banana', 'melon'] * 2,
    'ves': ['low', 'high'] * 3,
    'price': np.random.randint(0, 100, 6)
})

# Объединяем DataFrame по двум столбцам с помощью метода merge()
merged_df = pd.merge(df1, df2, how='inner', left_on=['fruit', 'weight'], right_on=['frukt', 'ves'])

# Удаляем лишние столбцы, оставляем только один из столбцов с ценой
merged_df = merged_df.drop(['frukt', 'ves'], axis=1)

print("Объединенный DataFrame с общими строками:")
print(merged_df)
