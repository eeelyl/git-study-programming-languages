import numpy as np

# Устанавливаем seed для воспроизводимости результатов
np.random.seed(10)

# Создаем массив
a = np.random.randint(0, 7, 10)
print("Исходный массив:")
print(a)

# Получаем уникальные значения и их количество
unique_values, counts = np.unique(a, return_counts=True)

# Создаем массив сначала заполнив его значениями True
result = np.full_like(a, False, dtype=bool)

# Идем по уникальным значениям и отмечаем как False, начиная со второго вхождения
for value in unique_values:
    indices = np.where(a == value)[0]  # Индексы элементов со значением value
    result[indices[1:]] = True  # Отмечаем как False начиная со второго вхождения

print("Повторяющиеся значения (начиная со второго вхождения) отмечены как False:")
print(result)
