def sort1(s):
    res = ''
    pos = list(filter(lambda x: int(x) >= 0, s.split(' ')))[::-1]
    neg = list(filter(lambda x: int(x) < 0, s.split(' ')))[::-1]
    for i in range(len(pos)):
        res += pos.pop() + ' '
        if neg:
            res += neg.pop() + ' '
    res += ' '.join(neg)
    return res


def sort2(s):
    numbers = sorted(list(map(int, s.split(' '))))
    pos = [str(x) for x in numbers if x >= 0]
    neg = [str(x) for x in numbers if x < 0]
    res = ' '.join(pos) + ' ' + ' '.join(neg)
    return res


s = '6 -1 3 -5 -15 4 1 9 8 6 -3 -4 12 -10 7'

print(sort1(s))
print(sort2(s))
