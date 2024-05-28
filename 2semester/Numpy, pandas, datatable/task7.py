import numpy as np

# Ввод
a = np.arange(9).reshape(3, 3)

# Меняем местами строки 1 и 3
a[[0, 2]] = a[[2, 0]]

print("Массив после замены строк:")
print(a)
