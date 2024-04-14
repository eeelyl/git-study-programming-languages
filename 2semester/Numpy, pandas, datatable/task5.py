import pandas as pd
import numpy as np

# Создаем DataFrame
df = pd.DataFrame(np.random.randint(1, 10, 16).reshape(4, 4),
                  columns=list('abcd'))

# Создаем пустой словарь для хранения частот уникальных значений
value_counts = {}

# Итерируемся по всем столбцам DataFrame
for col in df.columns:
    # Получаем частоту уникальных значений в текущем столбце
    col_value_counts = df[col].value_counts()
    
    # Обновляем словарь value_counts новыми значениями для текущего столбца
    value_counts[col] = col_value_counts

# Собираем все частоты в один DataFrame
result = pd.DataFrame(value_counts)

print("Частота уникальных значений во всем DataFrame:")
print(result)
