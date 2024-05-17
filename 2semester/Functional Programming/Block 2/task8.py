from typing import List, Tuple, Callable


def my_zip(list1: List[int], list2: List[int]) -> List[Tuple[int, int]]:
    """Группирует элементы двух списков, возвращая список кортежей."""
    return [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]


def concatenate_elements(zipped_list: List[Tuple[int, int]]) -> List[str]:
    """Конкатенирует элементы кортежей из списка."""
    return [f"{a}{b}" for a, b in zipped_list]


def sum_elements(zipped_list: List[Tuple[int, int]]) -> List[int]:
    """Складывает элементы кортежей из списка."""
    return [a + b for a, b in zipped_list]


def higher_order_function(list1: List[int], list2: List[int]) -> Tuple[Callable, Callable, Callable]:
    """Возвращает функции для группировки, конкатенации и сложения элементов списков."""
    zipped = my_zip(list1, list2)
    return (
        lambda: zipped,
        lambda: concatenate_elements(zipped),
        lambda: sum_elements(zipped)
    )

# Пример использования


def main():
    list1 = list(
        map(int, input("Введите первый список чисел, разделенных пробелами: ").split()))
    list2 = list(
        map(int, input("Введите второй список чисел, разделенных пробелами: ").split()))

    zip_func, concat_func, sum_func = higher_order_function(list1, list2)

    print("Сгруппированные элементы:", zip_func())
    print("Конкатенация элементов:", concat_func())
    print("Сложение элементов:", sum_func())


if __name__ == "__main__":
    main()
