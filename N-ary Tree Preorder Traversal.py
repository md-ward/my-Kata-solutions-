class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)


root = Node(10)

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)


