def max_of(lst):
    try:
        result = lst[0]
    except:
        print("Array is empty")
        return None
    for i in lst:
        if result < i:
            result = i
    return result

lst = [i for i in range(0,25)]
print(max_of(lst))