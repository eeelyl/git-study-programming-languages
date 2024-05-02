class Author:
    def __init__(self, full_name):
        self.full_name = full_name


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def view(self):
        print("Title:", self.title)
        print("Author:", self.author.full_name)
        print("Price:", self.price)


# Пример использования
author = Author("Lev Tolstoy")
book = Book("War and Peace", author, 25.99)

book.view()
