# Завдання 5. Візуалізація обходу бінарного дерева

# Використовуючи код із завдання 4 для побудови бінарного дерева, 
# необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
# Вона повинна відображати кожен крок у вузлах з різними кольорами, 
# використовуючи 16-систему RGB (приклад #1296F0). 
# Кольори вузлів мають змінюватися від темних до світлих відтінків, 
# залежно від послідовності обходу. Кожен вузол при його відвідуванні
#  має отримувати унікальний колір, який візуально відображає порядок обходу.
# Примітка. Використовуйте стек та чергу, НЕ рекурсію

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Розв'язок:

# Cтворюємо одиночний вузол бінарного дерева, зберігаючи унікальний ідентифікатор та колір.
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Додаємо вузли і ребра у граф, використовуючи ідентифікатори вузлів.
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Візуалізуємо бінарне дерево за допомогою "networkx" і "matplotlib"
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Генеруємо кольори для вузлів на основі кількості кроків обходу
def get_color(step):
    # Визначимо максимальні значення RGB
    max_color_value = 255
    
    # Зменшення насиченості у часі
    r = min(max_color_value, 100 + step * 15)  # Червоний
    g = min(max_color_value, 100 + step * 15)  # Зелений
    b = min(max_color_value, max_color_value - step * 10)  # Синій
    
    return f'#{r:02x}{g:02x}{b:02x}'

# Реалізуємо обходи дерева у глибину та в ширину відповідно. Вони змінюють колір кожного вузла під час обходу.
# Обхід дерева в глибину
def depth_first_traversal(root):
    stack = [root]
    step = 0
    while stack:
        node = stack.pop()
        if node:
            node.color = get_color(step)
            step += 1
            stack.append(node.right)
            stack.append(node.left)

# Обхід дерева в ширину
def breadth_first_traversal(root):
    queue = deque([root])
    step = 0
    while queue:
        node = queue.popleft()
        if node:
            node.color = get_color(step)
            step += 1
            queue.append(node.left)
            queue.append(node.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева після обхід у глибину
depth_first_traversal(root)
draw_tree(root)

# Відображення дерева після обхід в ширину
# Відновлення кольорів перед новим обходом
for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left]:
    node.color = "skyblue"  # Скидання кольорів для нового обходу

breadth_first_traversal(root)
draw_tree(root)