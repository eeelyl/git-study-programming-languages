import numpy as np
from functools import reduce
import math
import operator
import itertools

# Исходный список
list1 = [1, 2, 3]

# Метод 1: Используя numpy.prod()
method1 = np.prod(list1)

# Метод 2: Используя lambda function
method2 = reduce(lambda x, y: x * y, list1)

# Метод 3: Используя numpy.array
method3 = np.array(list1).prod()

# Метод 4: Используя prod function библиотеки math
method4 = math.prod(list1)

# Метод 5: Используя math.prod
method5 = math.prod(list1)

# Метод 6: Используя mul() function модуля operator
method6 = reduce(operator.mul, list1)

# Метод 7: Используя itertools.accumulate
method7 = list(itertools.accumulate(list1, operator.mul))[-1]

# Вывод результатов
print("Метод 1:", method1)
print("Метод 2:", method2)
print("Метод 3:", method3)
print("Метод 4:", method4)
print("Метод 5:", method5)
print("Метод 6:", method6)
print("Метод 7:", method7)
