import numpy as np

# Устанавливаем seed для воспроизводимости результатов
np.random.seed(10)

# Создаем массив
a = np.random.randint(1, 10, [3, 3])
print("Исходный массив:")
print(a)

# Находим минимальные значения в каждой строке
min_values = np.min(a, axis=1)

# Находим максимальные значения в каждой строке
max_values = np.max(a, axis=1)

# Делаем деление минимальных значений на максимальные
result = min_values / max_values

print("Результат деления минимального значения на максимальное в каждой строке:")
print(result)