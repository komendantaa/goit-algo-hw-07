from simle_binary_tree import tree

def sum_tree(node):
    if node is None:
        return 0  # Вузол порожній, повертаємо 0
    return node.key + sum_tree(node.left) + sum_tree(node.right)  # Рекурсивний підрахунок нащадків

print("Сума всіх значень у дереві:", sum_tree(tree))  # Виведе 67