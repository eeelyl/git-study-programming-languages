def set_gen(numbers):
    count = {}
    result = set()
    for num in numbers:
        if num in count:
            count[num] += 1
            result.add(str(num) * count[num])
        else:
            count[num] = 1
            result.add(num)
    return result
numbers = input("Введите список натуральных чисел через пробел: ").split()
numbers = [int(x) for x in numbers]
result5 = set_gen(numbers)
print(result5)