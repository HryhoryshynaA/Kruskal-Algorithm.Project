import random
import matplotlib
import networkx
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # вершини
        self.edges_record = [] # основна структура для зберігання
        self.adjacency_matrix = []   # матриця суміжності
        for i in range(len(vertices)):
            row = []
            for j in range(len(vertices)):
                row.append(0)
            self.adjacency_matrix.append(row)
        self.adjacency_list = {v: [] for v in vertices}  # список суміжності, де будуть дані по кожній вершині + ваги
    def add_edge(self, v1, v2, weight):
        self.edges_record.append((v1, v2, weight))
        self.adjacency_matrix[v1][v2] = weight
        self.adjacency_matrix[v2][v1] = weight


    def find_absolute_parent(self, vertex, parent): #рекурсивний пошук абсолютного батька/матері(жарт)
        if parent[vertex] == -1:
            return vertex
        return self.find_absolute_parent(parent[vertex], parent)

    def union(self, vertex_a, vertex_b, parent, rank):
        root_vertex_a = self.find_absolute_parent( vertex_a, parent)
        root_vertex_b = self.find_absolute_parent(vertex_b, parent)
        if rank[root_vertex_a] == rank[vertex_b]:  # якщо однаковий ранк, то тоді ми самі обираємо з якої на яку вершину посилатися
            parent[vertex_b] = root_vertex_a
            rank[root_vertex_a] += 1  # тому що ранки одинакові при обʼєднанні ранк потрбіно збільшити на одиницю
        elif rank[root_vertex_a] > rank[root_vertex_b]:  # порівнюємо ранки щоб ми знали що буде новим абсолютним рутом
            parent[root_vertex_b] = root_vertex_a
        elif rank[root_vertex_a] < rank[root_vertex_b]:
            parent[root_vertex_a] = root_vertex_b

    def generate_graph(num_vertices, density):
        vertices = list(range(num_vertices))
        graph = Graph(vertices)
        max_edges = num_vertices * (num_vertices - 1) / 2
        max_possible_edges = max_edges * density
        for u in range(num_vertices):
            for v in range(u + 1, num_vertices):
                if random.random() < max_possible_edges / max_edges:
                    weight = random.randint(1, 50)
                    graph.add_edge(u, v, weight)
        return graph


def kruskal(graph):
    sorted_edges = sorted(graph.edges_record, key=lambda x: x[2])
    smallaest_spanning_tree = set()
    parent = {}
    rank = {}
    for v in graph.vertices:
        parent[v] = -1
        rank[v] = 0
    for edge in sorted_edges:
        v1, v2, w = edge
        root_v1 = graph.find_absolute_parent(v1, parent)
        root_v2 = graph.find_absolute_parent(v2, parent)
        if root_v1 != root_v2:
            smallaest_spanning_tree.add((v1, v2, w))
            graph.union(v1, v2, parent, rank)
    return smallaest_spanning_tree

graph = Graph.generate_graph(10, 0.8)
minimum_spanning_tree = kruskal(graph)
print(graph.edges_record)
print(minimum_spanning_tree)