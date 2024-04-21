def most_long_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            words = f.read().split()
            if not words:
                print("Файл пуст.")
                return
            max_length = len(max(words, key=len))
            longest_words = [word for word in words if len(word) == max_length]
            if len(longest_words) == 1:
                print("Слово с максимальной длиной:")
            else:
                print("Слова с максимальной длиной:")
            for word in longest_words:
                print(word)
    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования функции
most_long_words('example.txt')
