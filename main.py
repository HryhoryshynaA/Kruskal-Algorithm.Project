class Graph:
    def __init__(self, vertices):
        self.vertices = vertices # вершини
        self.edges = [] # ребра
        self.adjacency_matrix = ""   # матриця суміжності
        self.adjacency_list = "" # список суміжності

    def find_absolute_parent(self, verce, parent):#рекурсивний пошук абсолютного батька/матері(жарт)
        if parent[verce] == -1:
            return verce
        self.find_absolute_parent(parent[verce], parent)

    def union(self):
        return "updated set"

    def kruskal(self):
        return "smallest spanning tree"

