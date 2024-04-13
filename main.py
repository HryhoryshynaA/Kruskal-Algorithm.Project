class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # вершини
        self.edges = [] # ребра
        self.adjacency_matrix = ""   # матриця суміжності
        self.adjacency_list = {v: [] for v in vertices} # список суміжності: це у нас словник, де вершина буде мати відповідну характеристику

    def find_absolute_parent(self, vertice, parent):#рекурсивний пошук абсолютного батька/матері(жарт)
        if parent[vertice] == -1:
            return vertice
        self.find_absolute_parent(parent[vertice], parent)

    def union(self, vertice_a, vertice_b, parent, rank):
        root_vertice_a = self.find_absolute_parent(parent, vertice_a)
        root_vertice_b = self.find_absolute_parent(parent, vertice_b)
        if rank[root_vertice_a] == rank[vertice_b]: # якщо один ранк, то тоді ми самі обираємо з якої на яку вершину посилатися
            parent[vertice_b] = root_vertice_a
            rank[root_vertice_a] += 1 #тому що ранки одинакові при обʼєднанні ранк потрбіно збільшити на одиницю
        elif rank[root_vertice_a] > rank[root_vertice_b]: # порівнюємо ранки щоб ми знали що буде новим абсолютним рутом
            parent[root_vertice_b] = root_vertice_a
        elif rank[root_vertice_a] < rank[root_vertice_b]:
            parent[root_vertice_a] = root_vertice_b


    def kruskal(self):
        return "smallest spanning tree"

