from functools import cmp_to_key


def compare_numbers(x, y):
    x, y = int(x), int(y)
    if x >= 0 and y >= 0:
        return x - y
    elif x < 0 and y < 0:
        return x - y
    elif x >= 0:
        return -1
    else:
        return 1


numbers = '6 -1 3 -5 -15 4 1 9 8 6 -3 -4 12 -10 7'.split()
sorted_numbers = sorted(numbers, key=cmp_to_key(compare_numbers))
print(' '.join(sorted_numbers))
