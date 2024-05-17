def my_filter(predicate, iterable):
    """Фильтрует элементы в iterable, оставляя только те, для которых predicate возвращает True."""
    return [item for item in iterable if predicate(item)]


def my_enumerate(iterable, start=0):
    """Возвращает кортежи (индекс, элемент) из iterable, начиная с указанного start."""
    index = start
    for item in iterable:
        yield index, item
        index += 1


def main():
    # Получаем список слов от пользователя
    words = input("Введите список слов, разделенных пробелами: ").split()
    # Получаем букву от пользователя
    letter = input("Введите букву: ").strip().lower()

    # Используем my_filter для фильтрации слов, начинающихся с заданной буквы
    filtered_words = my_filter(
        lambda word: word.lower().startswith(letter), words)

    # Выводим результаты с использованием my_enumerate
    for index, word in my_enumerate(filtered_words, start=1):
        print(f"{index}-e слово нового списка - {word}")


if __name__ == "__main__":
    main()
