import numpy as np

lst = [12, 14, 95, 3, 73]
a = np.array(lst)
print(a[a % 2 != 0])
