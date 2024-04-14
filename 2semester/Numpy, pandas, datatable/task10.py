import numpy as np

# Ввод
a = np.random.randint(100, size=10)
print("Исходный массив:")
print(a)

# Используем argsort для получения индексов элементов в отсортированном порядке
indices = np.argsort(a)

# Создаем массив, в котором значения - это ранги элементов
ranked = np.empty_like(indices)
ranked[indices] = np.arange(len(a))

print("Отранжированный массив:")
print(ranked)
