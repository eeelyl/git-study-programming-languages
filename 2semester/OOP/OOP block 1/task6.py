class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Стек пустой")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Стек пустой")

    def display(self):
        if not self.is_empty():
            print("Элементы стека:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Стек пустой")


# Пример использования
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()

print("Извлечение элемента из стека:", stack.pop())
print("Извлечение элемента из стека:", stack.pop())

stack.display()
