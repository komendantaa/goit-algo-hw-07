from simle_binary_tree import tree

def find_max(node):
    if node is None:
        return None  # Дерево порожнє

    current = node
    while current.right is not None:  # Рухаємось до крайнього правого вузла
        current = current.right
    return current.key  # Повертаємо ключ найбільшого елемента

print("Найбільший елемент у дереві:", find_max(tree))  # Виведе 30
