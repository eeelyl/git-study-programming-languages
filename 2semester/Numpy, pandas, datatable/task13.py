import numpy as np

# Ввод
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

# Вносим некоторые случайные значения NaN
np.random.seed(42)
iris[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

print("Исходный массив:")
print(iris)

# Находим строки, содержащие nan
rows_with_nan = np.isnan(iris).any(axis=1)

# Удаляем строки с nan
iris_without_nan = iris[~rows_with_nan]

print("\nМассив без строк, содержащих nan:")
print(iris_without_nan)
