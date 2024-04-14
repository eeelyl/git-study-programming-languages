import numpy as np

# Ввод
a = np.arange(9).reshape(3, 3)

# Меняем местами строки 1 и 3
a[[1, 2]] = a[[2, 1]]

print("Массив после замены строк:")
print(a)
