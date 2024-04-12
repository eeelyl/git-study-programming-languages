# Анна решила представить некую таблицу с заглавными и строчными буквами русского алфавита в красивом формате.
# Об этом ее попросили англоязычные друзья из социальных сетей.
# Недолго думая девушка создала скрипт, который выполнял подобную операцию. Результат работы программы продемонстрирован ниже.
# Сможете повторить (в строках с галочками - их 27 штук, чтобы вам не пришлось долго считать)
# Для идентичности результатов примените любой моноширинный шрифт (в котором все символы имеют одинаковую ширину).

rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for position in range(11):
    print('^' * 27)
    for letter in rus_lower:
        if rus_lower.index(letter) % 11 == position:
            print('| ', letter.upper(), letter, ' |', end='')
    print()
print('^' * 27)
