import numpy as np
import pandas as pd

a = pd.Series([2, 4, 6, 8])
b = pd.Series([1, 3, 5, 7])

diff = a - b

squared_diff = diff ** 2

sum_squared_diff = squared_diff.sum()

euclidean_distance = np.sqrt(sum_squared_diff)

print("Евклидово расстояние между точками a и b:", euclidean_distance)
