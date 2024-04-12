from collections.abc import Hashable


def list_to_set(lst):
    st = {item for item in lst if isinstance(item, Hashable)}
    print(st)


print(list_to_set([1, [2], [3, 4, 5, 6], 11]))
