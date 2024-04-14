import pandas as pd
import numpy as np

# Ввод данных
df = pd.DataFrame(np.random.randint(1, 100, 16).reshape(4, 4), columns=list('efgh'), index=list('abcd'))

# Функция для вычисления евклидова расстояния между строками
def euclidean_distance(row1, row2):
    return np.linalg.norm(row1 - row2)

# Создание нового столбца для номера ближайшей строки и расстояния
nearest_row = []
dist = []

for index, row in df.iterrows():
    # Вычисляем расстояния между текущей строкой и всеми остальными строками
    distances = [euclidean_distance(row, df.loc[i]) for i in df.index if i != index]
    # Находим индекс строки с минимальным расстоянием
    nearest_index = np.argmin(distances)
    # Добавляем номер ближайшей строки и значение расстояния в списки
    nearest_row.append(df.index[nearest_index])
    dist.append(distances[nearest_index])

# Добавляем новые столбцы к DataFrame
df['nearest_row'] = nearest_row
df['dist'] = dist

print(df)
