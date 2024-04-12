import numpy as np
start = int(input('Start: '))
end = int(input('End: '))
a = np.array([i for i in range(start, end+1)])
print(a[a % 2 == 0])
