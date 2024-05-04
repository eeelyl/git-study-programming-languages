def flatten_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result


def flatten_iterative(lst):
    result = []
    stack = lst[::-1]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)
    return result


sp = [[[5, 7, 2], [4, 9, 5]], [[2, 5, 4]], [[3, 2, 1], [[5], [9, 5]]],
      [4, 3, 1, 2], [[4, 7, 2], [6, 4]], [[[4, 1, 6], [3, 8]], [4, 5]],
      [9, 1], [3, 1], [[5, 6], [[4, 2, 1], [2, 5], [[6, 8, 2, 3, 4]]]],
      [5, 3, 2], [2, [1], 4], [2, 5, [4, 3, 1], 6, 7, [9, 0, 5, 2, 4]],
      [7, 3, [4]], [4, 2, [[[5, 6, 7], 5, 7]], 1], [3, 4, 6, [6, 4, 5]],
      ]

print(flatten_recursive(sp))
print(flatten_iterative(sp))
