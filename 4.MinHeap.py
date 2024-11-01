# Завдання 4. Візуалізація піраміди

# Наступний код виконує побудову бінарних дерев. 
# Виконайте аналіз коду, щоб зрозуміти, як він працює.
# Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.

# Розв'язок

import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Створює вузол дерева з властивостями `val`, `left`, `right`, `color` і унікальним `id`.
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

#  Додає вузли та ребра до графа, створюючи структуру для подальшої візуалізації.
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

# Функція `draw_heap`**: Використовує `networkx` для малювання графа, відображаючи допоміжні дані про бінарну купу.
def draw_heap(heap_root):
    heap_graph = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap_graph = add_edges(heap_graph, heap_root, pos)

    colors = [node[1]['color'] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap_graph.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap_graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Додаємо клас для побудови бінарної купи
class MinHeap:
    def __init__(self):
        self.root = None
        self.nodes = []

# Вставляє новий вузол у купу, забезпечуючи (у базовій версії) збереження властивості мінімальної купи.
    def insert(self, key):
        new_node = Node(key)
        self.nodes.append(new_node)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

# Рекурсивно вставляє кінцевий вузол на потрібне місце
    def _insert(self, node, new_node):
        if new_node.val < node.val:
            node.val, new_node.val = new_node.val, node.val  # Міняємо значення
        if not node.left:
            node.left = new_node
        elif not node.right:
            node.right = new_node
        else:
            # Вставка в лівий або правий підвузол
            if len(self.nodes) % 2 == 0:  # Зліва
                self._insert(node.left, new_node)
            else:  # Справа
                self._insert(node.right, new_node)

# Приклад 
heap = MinHeap()
heap.insert(20)
heap.insert(8)
heap.insert(30)
heap.insert(6)
heap.insert(16)

# Відображення бінарної купи
draw_heap(heap.root)