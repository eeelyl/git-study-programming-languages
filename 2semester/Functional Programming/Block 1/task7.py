import random

class CardDeck:
    def __init__(self):
        # Создаем список всех возможных карт в колоде
        suits = ['Пик', 'Треф', 'Бубен', 'Черв']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.cards = [(value, suit) for suit in suits for value in values]

    def shuffle(self):
        # Перемешиваем карты в колоде
        random.shuffle(self.cards)

    def __iter__(self):
        # Возвращаем итератор для перебора карт в колоде
        self._index = 0
        return self

    def __next__(self):
        # Проверяем, что есть еще карты для перебора
        if self._index < len(self.cards):
            card = self.cards[self._index]
            self._index += 1
            return card
        else:
            # Если карты закончились, вызываем исключение StopIteration
            raise StopIteration

# Пример использования
deck = CardDeck()
deck.shuffle()

print("Перебор колоды карт:")
for card in deck:
    print(card)
