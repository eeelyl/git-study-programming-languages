class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = "Николай"
        if name != "Николай":
            print("Я не", name, ", а Николай")


# Пример использования
nikola = Nikola("Максим", 25)
print("Имя:", nikola.name)
