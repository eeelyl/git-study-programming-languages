import numpy as np

# Ввод
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Извлекаем значения petallength и species
petal_lengths = iris[:, 2].astype(float)
species = iris[:, 4]

# Фильтруем только вид setosa
setosa_petal_lengths = petal_lengths[species == b'Iris-setosa']

# Находим уникальные значения длины лепестка setosa и сортируем их в порядке убывания
unique_setosa_petal_lengths = np.unique(setosa_petal_lengths)[::-1]

# Второе максимальное значение будет вторым по величине элементом
second_max_setosa_petal_length = unique_setosa_petal_lengths[1]

print("Второе максимальное значение petallength для вида setosa:", second_max_setosa_petal_length)
