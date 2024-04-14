import numpy as np

# Ввод
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Извлекаем столбец species
species_column = iris[:, 4]

# Находим уникальные значения и их количество
unique_values, counts = np.unique(species_column, return_counts=True)

# Выводим уникальные значения и их количество
print("Уникальные значения в столбце species:", unique_values)
print("Количество уникальных значений в столбце species:", counts)
