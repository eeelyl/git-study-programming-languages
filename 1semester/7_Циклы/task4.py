# Для идентификации своего круга проверенных лиц будущий тайный агент (ведь все о чем-то мечтают)
# Максим решил пускать на свою страничку в Интернете только тех, чьи никнеймы есть в его секретном списке.
# Он уверен в своих людях (особенно в том, что они по глупости не расскажут никому своё секретное прозвище),
# как и в том, что имена товарищей невозможно подобрать случайно.
# К слову, вот этот список: Мавпродош, Лорнектиф, Древерол, Фиригарпиг, Клодобродыч.
# По мере увеличения круга знакомых Максим, естественно, дополнит данный список.
# Ваша задача такова: повторите код, который будет спрашивать у пользователя его ник и либо пускать на сайт
# (выведется сообщение Ты – свой. Приветствую, любезный {НИК_ПОСЕТИТЕЛЯ}!),
# либо нет (в этом случае будет такой текст: Тут ничего нет. Еще есть вопросы?.
# Фактически, будущий супергерой решил поиздеваться над теми, кого нет в его удивительном перечне, так как им будет показываться это сообщение постоянно.
# Очень коварный замысел!).
# Для проверки прозвищ посетителей используйте встроенную функцию input().

nick = input()
secret_list = ['Мавпродош', 'Лорнектиф',
               'Древерол', 'Фиригарпиг', 'Клодобродыч']
while nick not in secret_list:
    print('Тут ничего нет. Еще есть вопросы?')
    nick = input('Введите свой ник: ')
else:
    print(f'Ты – свой. Приветствую, любезный {nick}!')
