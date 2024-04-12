import numpy as np


def remove_func(lst, var=1):
    if var == 1:
        a = np.array(lst)
        return list(a[a % 5 != 0]), list(a[a % 5 == 0])
    elif var == 2:
        return '[1:5]', lst[:1:] + lst[5::]


lst1 = [12, 15, 3, 10]
lst2 = [11, 5, 17, 18, 23, 50]

remove1, new_list1 = remove_func(lst1, var=1)
remove2, new_list2 = remove_func(lst2, var=2)
print(f'Remove = {remove1}, New_list = {new_list1}')
print(f'Remove = {remove2}, New_list = {new_list2}')
