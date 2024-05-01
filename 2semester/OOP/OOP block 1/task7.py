class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Связанный список пустой")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        if self.head is None:
            print("Связанный список пустой, невозможно удалить элемент")
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == key:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print("Элемент не найден в связанном списке")

# Пример использования
linked_list = LinkedList()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_beginning(4)

print("Связанный список:")
linked_list.display()

linked_list.delete_node(3)

print("Связанный список после удаления элемента 3:")
linked_list.display()
