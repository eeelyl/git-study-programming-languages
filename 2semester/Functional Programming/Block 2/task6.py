def predicate(word):
    """Функция-предикат проверяет совпадение первой и последней буквы слова."""
    return word[0] == word[-1] if word else False


def my_filter(func, iterable):
    """Функция-фильтр, аналог встроенной filter()."""
    return [item for item in iterable if func(item)]

# Пример использования


def main():
    input_str = input("Введите список слов, разделенных пробелами: ")
    words = input_str.split()

    filtered_words = my_filter(predicate, words)
    print(" ".join(filtered_words))


if __name__ == "__main__":
    main()
