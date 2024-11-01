# Завдання 3. Дерева, алгоритм Дейкстри

#Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
# використовуючи бінарну купу. Завдання включає створення графа, 
# використання піраміди для оптимізації вибору вершин та обчислення 
# найкоротших шляхів від початкової вершини до всіх інших.

# Розв'язок:

import heapq

def dijkstra(graph, start):

    # Створюю граф, який представляє собою список суміжності
    # Створюю масив "dist". Далі встановлюю всі значення в "∞", за винятком початкової вершини, вона = 0`.
    # Створюю бінарну купу для зберігання вершин графа, упорядкованих за відстанню.

    dist = {vertex: float('infinity') for vertex in graph}
    dist[start] = 0
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue: # Створюю цикл
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо відстань до випадкової вершини більше, ніж вже знайдена, пропускаємо
        if current_distance > dist[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусідньої вершини
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist

# Приклад графа як словник
graph = {
    'A': {'B': 3, 'C': 12},
    'B': {'A': 3, 'C': 6, 'D': 15},
    'C': {'A': 12, 'B': 6, 'D': 3},
    'D': {'B': 15, 'C': 3}
}

# Виклик алгоритму Дейкстри
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)
print(shortest_paths)