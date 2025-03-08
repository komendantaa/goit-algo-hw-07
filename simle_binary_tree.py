from typing import Optional

class Node:
    def __init__(self, key):
        self.key = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

tree = Node(20)
tree.left = Node(10)
tree.right = Node(30)
tree.left.left = Node(5)
tree.left.left.left = Node(2)