class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)

    def __repr__(self):
        return "House({}, {})".format(self._area, self._price)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


class Human:
    default_name = "John"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self._money = 0
        self._house = None

    def info(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Money: {self._money}, House: {self._house}")

    @staticmethod
    def default_info():
        print(
            f"Default Name: {Human.default_name}, Default Age: {Human.default_age}")

    def make_deal(self, house, price):
        self._money -= price
        self._house = house

    def earn_money(self, amount):
        self._money += amount

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if final_price > self._money:
            print("Not enough money to buy the house.")
        else:
            self.make_deal(house, final_price)
            print("House successfully purchased!")


# Пункт IV: Тестирование решения
# 1. Вызовите справочный метод default_info() для класса Human.
Human.default_info()

# 2. Создайте объект класса Human.
person = Human(name="Alice", age=25)

# 3. Выведите справочную информацию о созданном объекте (вызовите метод info()).
person.info()

# 4. Создайте объект класса SmallHouse.
small_house = SmallHouse(price=50000)

# 5. Попробуйте купить созданный дом, убедитесь в получении предупреждения.
person.buy_house(small_house, discount=0.1)

# 6. Поправьте финансовое положение объекта - вызовите метод earn_money().
person.earn_money(60000)

# 7. Снова попробуйте купить дом.
person.buy_house(small_house, discount=0.1)

# 8. Посмотрите, как изменилось состояние объекта класса Human.
person.info()
