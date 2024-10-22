# Составьте функцию season_events(number_of_month), которая принимает номер месяца вашего рождения и в зависимости от сезона печатает на выходе следующее:
# Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>.
# В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона:
# - для зимы За окном падал белый снег,- для весны Птицы пели прекрасные песни,- для лета Солнце светило ярче чем когда-либо,- для осени Урожай был невероятным.
# Важно учесть, что пользователи могут ввести любой тип данных в качестве аргумента (не попадитесь на этом и предупредите о том, что Требуется ввести реальный номер месяца).

def season_events(number_of_month):
    months = {1: 'январе', 2: 'феврале', 3: 'марте', 4: 'апреле', 5: 'мае', 6: 'июне',
              7: 'июле', 8: 'августе', 9: 'сентябре', 10: 'октябре', 11: 'ноябре', 12: 'декабре'}
    if int(number_of_month) in range(1, 13):
        if number_of_month in range(3, 6):
            print(f'Вы родились в {
                  months[int(number_of_month)]}. Птицы пели прекрасные песни')
        elif number_of_month in range(6, 9):
            print(f'Вы родились в {
                  months[int(number_of_month)]}. Солнце светило ярче чем когда-либо')
        elif number_of_month in range(9, 12):
            print(f'Вы родились в {
                  months[int(number_of_month)]}. Урожай был невероятным')
        else:
            print(f'Вы родились в {
                  months[int(number_of_month)]}. За окном падал белый снег')
    else:
        print('Требуется ввести реальный номер месяца')


number_of_month = int(input('Введите номер месяца вашего рождения: '))
season_events(number_of_month)
