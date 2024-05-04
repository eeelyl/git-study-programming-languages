from functools import *
import math


def solve1(lst):
    a = reduce(lambda x, y: x * y, lst)
    return a


def solve2(lst):
    return math.prod(lst)


def solve3(lst):
    res = 1
    for x in lst:
        res *= x
    return res


lst = [1, 2, 3]

print(solve1(lst))
print(solve2(lst))
print(solve3(lst))
