# Николай написал функцию is_alive(health), которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, то функция возвращает False, в противном случае True.
# К сожалению, функция не работает, так как ученик допустил в ней ряд ошибок.
# Исправьте их и проверьте работоспособность программы (в качестве аргумента всегда передается число).

def is_alive(health):
    if health <= 0:
        return False
    else:
        return True


health = int(input())
print(is_alive(health))
