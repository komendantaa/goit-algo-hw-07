from simle_binary_tree import tree

def find_min(node):
    if node is None:
        return None  # Дерево порожнє

    current = node
    while current.left is not None:  # Рухаємось до крайнього лівого вузла
        current = current.left
    return current.key  # Повертаємо ключ найменшого елемента

print("Найменший елемент у дереві:", find_min(tree))  # Виведе 2