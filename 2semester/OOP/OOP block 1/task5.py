class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def search_key(self, key):
        return self.search(self.root, key)


# Пример использования
tree = BinarySearchTree()
tree.insert_key(50)
tree.insert_key(30)
tree.insert_key(20)
tree.insert_key(40)
tree.insert_key(70)
tree.insert_key(60)
tree.insert_key(80)

result = tree.search_key(70)
if result:
    print("Элемент найден:", result.val)
else:
    print("Элемент не найден")
