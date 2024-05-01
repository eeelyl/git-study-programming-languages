class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def size(self):
        return len(self.items)

# Пример использования:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue size:", q.size())

print("Dequeued item:", q.dequeue())
print("Dequeued item:", q.dequeue())
print("Queue size after dequeue:", q.size())
