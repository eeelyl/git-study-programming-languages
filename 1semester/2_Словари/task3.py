# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

def count_it(sequence):
    # Создаем словарь для подсчета количества каждой цифры
    count_dict = {}

    # Проходимся по каждому символу в строке
    for digit in sequence:
        # Преобразуем символ в целое число
        digit_int = int(digit)
        # Увеличиваем счетчик для данной цифры
        count_dict[digit_int] = count_dict.get(digit_int, 0) + 1

    # Сортируем словарь по значениям в убывающем порядке
    sorted_counts = sorted(
        count_dict.items(), key=lambda x: x[1], reverse=True)

    # Выбираем три самых часто встречающихся числа
    top_three = sorted_counts[:3]

    # Преобразуем результат в словарь для возврата из функции
    result_dict = dict(top_three)

    return result_dict


# Пример использования функции
sequence = "4444333221"
result = count_it(sequence)
print("Словарь из трех самых часто встречаемых чисел:")
print(result)
