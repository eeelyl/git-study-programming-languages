class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return '{} : {}'.format(self.name, self.value)


class ShoppingCart:

    def __init__(self, *items):
        self.total = 0
        self.storage = []
        for item in items:
            self.total += item.value
            self.storage.append(item)

    def add_item(self, item):
        self.total += item.value
        self.storage.append(item)

    def remove_item(self, item):
        if item in self.storage:
            self.total -= item.value
            self.storage.remove(item)

    def __str__(self):
        res = ''
        for item in self.storage:
            res += item.__str__() + ', '
        res += f'Total : {self.total}'
        return res


carrot = Item('Carrot', 15)
ice_cream = Item('Ice cream', 20)
coke = Item('Coca-cola', 25)
bread = Item('bread', 5)

cart = ShoppingCart(carrot, ice_cream, coke)
print(cart)
cart.add_item(bread)
print(cart)
cart.remove_item(ice_cream)
print(cart)
