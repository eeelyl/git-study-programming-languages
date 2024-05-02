class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof"

    def wag_tail(self):
        return f"{self.name} is wagging its tail"


class Cat(Animal):
    def sound(self):
        return "Meow"

    def purr(self):
        return f"{self.name} is purring"


def make_sound(animal):
    return animal.sound()


dog = Dog("Buddy")
cat = Cat("Whiskers")

# Проверка метода sound с объектом Dog
print("Dog sound:", make_sound(dog))
print(dog.wag_tail())

# Проверка метода sound с объектом Cat
print("Cat sound:", make_sound(cat))
print(cat.purr())
