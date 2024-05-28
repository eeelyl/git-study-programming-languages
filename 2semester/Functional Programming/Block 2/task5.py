def higher_order_function(numbers):
    def multiply_elements(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def sum_elements(lst):
        result = 0
        for num in lst:
            result += num
        return result

    if len(numbers) % 2 == 0:
        return multiply_elements
    else:
        return sum_elements

# Пример использования


def main():
    # 8 9 3 5 1 3 8 2 9
    # 7 3 2 8 9 1 2 3 4 6
    input_str = input("Введите список чисел, разделенных пробелами: ")
    numbers = list(map(int, input_str.split()))

    operation = higher_order_function(numbers)

    if len(numbers) % 2 == 0:
        result = operation(numbers)
        print(f"Количество чисел четное, результат: {result}")
    else:
        result = operation(numbers)
        print(f"Количество чисел нечетное, результат: {result}")


if __name__ == "__main__":
    main()
