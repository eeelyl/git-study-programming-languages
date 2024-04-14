import numpy as np
# Создайте вектор с элементами от 12 до 42:
vector = np.arange(12, 43)

# Создайте вектор из нулей длины 12, но его пятый элемент должен быть равен 1:
vector = np.zeros(12)
vector[4] = 1

# Создайте матрицу (3, 3), заполненную от 0 до 8:
matrix = np.arange(9).reshape(3, 3)

# Найдите все положительные числа в np.array([1,2,0,0,4,0]):
array = np.array([1, 2, 0, 0, 4, 0])
positive_numbers = array[array > 0]

# Умножьте матрицу размерности (5, 3) на (3, 2):
matrix1 = np.random.rand(5, 3)
matrix2 = np.random.rand(3, 2)
result = np.dot(matrix1, matrix2)

# Создайте матрицу (10, 10) так, чтобы на границе были 0, а внутри 1:
matrix = np.ones((10, 10))
matrix[1:-1, 1:-1] = 0

# Создайте рандомный вектор и отсортируйте его:
vector = np.random.rand(10)
sorted_vector = np.sort(vector)

# Каков эквивалент функции enumerate для numpy массивов?
array = np.array(['a', 'b', 'c', 'd'])
for index, value in np.ndenumerate(array):
    print(index, value)

# Создайте рандомный вектор и выполните нормализацию столбцов 
# (из каждого столбца вычесть среднее этого столбца, 
# из каждого столбца вычесть sd этого столбца):
matrix = np.random.rand(3, 3)
normalized_matrix = (matrix - np.mean(matrix, axis=0)) / np.std(matrix, axis=0)
# Для заданного числа найдите ближайший к нему элемент в векторе. 
# Найдите N наибольших значений в векторе:
vector = np.array([1, 3, 5, 7, 9])
number = 6
closest_value = vector[np.abs(vector - number).argmin()]

N = 3
top_N_values = np.sort(vector)[-N:]
