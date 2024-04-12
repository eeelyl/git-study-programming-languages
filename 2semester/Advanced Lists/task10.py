def remove_empty_tuples(tuple_list):
    # Используя генератор списка
    method1 = [tup for tup in tuple_list if tup]

    # Используя функцию filter() в сочетании с лямбда-функцией
    method2 = list(filter(lambda x: x, tuple_list))

    # Используя цикл for
    method3 = []
    for tup in tuple_list:
        if tup:
            method3.append(tup)

    # Используя метод filter() и None в качестве функции
    method4 = list(filter(None, tuple_list))

    # Используя генераторное выражение с функцией bool()
    method5 = [tup for tup in tuple_list if bool(tup)]

    return method1, method2, method3, method4, method5

tuples = [('','','8'), (), ('0', '00', '000'), ('birbal', '', '45'), (''), (),  ('',''),()]
# tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', ''), ()]
results = remove_empty_tuples(tuples)
print("Method 1:", results[0])
print("Method 2:", results[1])
print("Method 3:", results[2])
print("Method 4:", results[3])
print("Method 5:", results[4])
