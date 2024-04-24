import os


def print_content(directory):
    try:
        for root, dirs, files in os.walk(directory):
            print(f"Папка: {root}")
            if dirs:
                print("Подкаталоги:")
                for d in dirs:
                    print(os.path.join(root, d))
            if files:
                print("Файлы:")
                for f in files:
                    print(os.path.join(root, f))
            print("-" * 30)
    except FileNotFoundError:
        print(f"Директория '{directory}' не найдена.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования функции
print_content(r'C:\Users\chel\Documents\code\git-study-programming-languages')
