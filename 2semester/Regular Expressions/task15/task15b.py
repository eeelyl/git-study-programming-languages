import re

def remove_ansi_escape_sequences(text):
    return re.sub(r'\033\[[0-9;]+m', '', text)

# Пример использования:
text = "This is \033[31mred\033[0m text with \033[1mBold\033[0m formatting."
result = remove_ansi_escape_sequences(text)
print("Результат без управляющих последовательностей ANSI:", result)
