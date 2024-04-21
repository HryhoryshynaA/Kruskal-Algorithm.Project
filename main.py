import random
import networkx as nx
import matplotlib.pyplot as plt
import time
import os

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.adjacency_list = {v: [] for v in vertices}
        self.adjacency_matrix = [[0] * len(self.vertices) for _ in range(len(self.vertices))]

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))
        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        minimum_spanning_tree = set()
        parent = {}
        rank = {}
        for v in self.vertices:
            parent[v] = v
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

    def visualize(self, output_dir, trial_number, num_vertices, density):
        output_file = os.path.join(output_dir, f"Trial_{trial_number}_Graph_{num_vertices}_{density}.png")
        G = nx.Graph()
        for edge in self.edges:
            u, v, weight = edge
            G.add_edge(u, v, weight=weight)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=10, node_color="purple", font_color="white")
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Graph Visualization")
        plt.savefig(output_file)
        plt.close()

    def print_adjacency_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adjacency_matrix:
            print(row)

def generate_random_graph(num_vertices, density):
    vertices = list(range(num_vertices))
    g = Graph(vertices)
    max_edges = num_vertices * (num_vertices - 1) // 2
    num_edges = int(density * max_edges)
    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        while u == v or (u, v, _) in g.edges:
            u = random.randint(0, num_vertices - 1)
            v = random.randint(0, num_vertices - 1)
        weight = random.randint(1, 100)
        g.add_edge(u, v, weight)
    return g


def experiment(num_vertices_list, density_list, num_trials, output_directory):
    for num_vertices in num_vertices_list:
        for density in density_list:
            for trial in range(1, num_trials + 1):
                random_graph = generate_random_graph(num_vertices, density)
                random_graph.visualize(output_directory, trial, num_vertices, density)

        trial_output_file = os.path.join("experiment_result.csv")

        with open(trial_output_file, "w") as f:
            f.write("NumVertices, Density, AvgKruskalTime(ms)\n")
            for num_vertices in num_vertices_list:
                for density in density_list:
                    total_time = 0
                    for _ in range(num_trials):
                        random_graph = generate_random_graph(num_vertices, density)
                        start_time = time.time()
                        _ = random_graph.kruskal()
                        end_time = time.time()
                        total_time += (end_time - start_time) * 1000
                    avg_time = total_time / num_trials
                    f.write(f"{num_vertices}, {density}, {avg_time}\n")
    print("Експерименти успішно проведені!")


num_vertices_list = [58, 20, 30, 45, 50, 84, 73, 69, 46, 24,]
density_list = [0.7, 0.8, 0.6, 0.4, 0.85]
num_trials = 20
directory = "Trial graphs"
if not os.path.exists(directory):
    os.makedirs(directory)
experiment(num_vertices_list, density_list, num_trials, directory)
