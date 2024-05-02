class Soda:
    def __init__(self, addon=None):
        if addon is not None and not isinstance(addon, str):
            raise TypeError("Добавка должна быть строкой")
        self.addon = addon

    def show_my_drink(self):
        if self.addon is not None:
            print(f"Газировка и {self.addon}")
        else:
            print("Обычная газировка")


# Пример использования
soda_with_addon = Soda("вишня")
soda_with_addon.show_my_drink()

soda_without_addon = Soda()
soda_without_addon.show_my_drink()
