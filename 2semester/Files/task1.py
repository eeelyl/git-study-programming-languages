def read_last_lines(lines, file):
    if lines <= 0:
        print("Количество строк должно быть положительным числом.")
        return

    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines_list = f.readlines()
            if lines >= len(lines_list):
                print("Запрошено больше строк, чем содержится в файле.")
                return
            last_lines = lines_list[-lines:]
            for line in last_lines:
                # Удаляем символ новой строки из каждой строки
                print(line.rstrip())
    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования функции
read_last_lines(3, 'example.txt')
