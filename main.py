class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # вершини
        self.edges = [] # ребра
        self.adjacency_matrix = []   # матриця суміжності
        self.adjacency_list = "" # список суміжності

        for i in range(len(vertices)):
            row = []
            for j in range(len(vertices)):
                row.append(0)
            self.adjacency_matrix.append(row)

    def add_edge(self, v1, v2, weight):
        self.adjacency_matrix[v1][v2] = weight
        self.adjacency_matrix[v2][v1] = weight

    def find_absolute_parent(self, verce, parent): #рекурсивний пошук абсолютного батька/матері(жарт)
        if parent[verce] == -1:
            return verce
        self.find_absolute_parent(parent[verce], parent)

    def union(self):
        return "updated set"

    def kruskal(self):
        return "smallest spanning tree"

    def kruskal(self):
        minimum_spanning_tree = set()
        parent = {}
        rank = {}
        for v in self.vertices:
            parent[v] = -1
            rank[v] = 0
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        for edge in sorted_edges:
            u, v, weight = edge
            root_u = self.find_parent(parent, u)
            root_v = self.find_parent(parent, v)
            if root_u != root_v:
                minimum_spanning_tree.add(edge)
                self.union(parent, rank, root_u, root_v)
        return minimum_spanning_tree  