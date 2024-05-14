def sort1(s):
    res = [int(num) for num in s.split()]
    res.sort(key=lambda x: (x < 0, x))
    return res


def sort2(s):
    res = [int(num) for num in s.split()]
    res.sort()
    return res


inp = '6 -1 3 -5 -15 4 1 9 8 6 -3 -4 12 -10 7'

print(sort1(inp))
print(sort2(inp))
