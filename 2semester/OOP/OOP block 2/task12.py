class Tomato:
    states = {
        'Отсутствует': 0,
        'Цветение': 1,
        'Зеленый': 2,
        'Красный': 3
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Пока не все помидоры созрели.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("- Регулярно поливайте растения.")
        print("- Удаляйте сорняки.")
        print("- Опрыскивайте растения от вредителей.")
        print("- Следите за стадиями созревания помидоров.")


# Пример использования
Gardener.knowledge_base()

tomato_bush = TomatoBush(5)
gardener = Gardener("Иван", tomato_bush)

for day in range(5):
    print(f"День {day + 1}:")
    gardener.work()
    gardener.harvest()
