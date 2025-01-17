import os
import time
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    # Constructor to intialize the graph
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.operations = 0  # Contor pentru numărul de operații

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, vertex, color, color_map):
        self.operations += 1
        for neighbor in self.graph[vertex]:
            if color_map.get(neighbor) == color:
                return False
        return True

    def color_graph(self, vertex, num_colors, color_map):
        if vertex == self.V:
            return True

        for color in range(num_colors):
            self.operations += 1
            if self.is_safe(vertex, color, color_map):
                color_map[vertex] = color
                if self.color_graph(vertex + 1, num_colors, color_map):
                    return True
                color_map[vertex] = -1

        return False

    def backtracking_coloring(self):
        color_map = {-1: -1}
        num_colors = 1
        self.operations = 0

        while not self.color_graph(0, num_colors, color_map):
            num_colors += 1
            color_map = {-1: -1}
        
        return num_colors, self.operations


def read_graph_from_file(file_path):
    edges = []
    nodes = set()

    with open(file_path, "r") as file:
        for line in file:
            u, v = map(int, line.split()[:2])  # Extract the two vertices
            edges.append((u, v))
            nodes.add(u)
            nodes.add(v)

    print(f"Reading graph from {file_path}...")
    num_vertices = max(nodes) + 1
    graph = Graph(num_vertices)
    for u, v in edges:
        graph.add_edge(u, v)

    return graph, len(edges), len(nodes)


def benchmark():
    input_dir = "input"
    categories = ["bipartite", "planar", "sparse", "random", "complete"]
    
    densities = []  # Densitățile grafurilor
    operations = []  # Numărul de operații
    
    max_colors = 30

    for category in categories:
        category_path = os.path.join(input_dir, category)

        for filename in os.listdir(category_path):
            if filename.endswith(".edgelist"):
                file_path = os.path.join(category_path, filename)
                graph, edge_count, node_count = read_graph_from_file(file_path)

                # Calculăm densitatea grafului
                if node_count > 1:
                    density = (2 * edge_count) / (node_count * (node_count - 1))
                    densities.append(density)

                    # Rulăm algoritmul și colectăm numărul de operații
                    num_colors, operations_count = graph.backtracking_coloring()
                    output_file = os.path.join("output", category, f"{os.path.splitext(filename)[0]}_output.txt")

	                # Scriem rezultatele în fișier
                    with open(output_file, "w") as f:
                        f.write(str(num_colors))
                    operations.append(operations_count)

    # Generăm graficul
    plt.figure(figsize=(10, 6))

    plt.scatter(densities, operations, color='skyblue', edgecolor='black')
    plt.xlabel("Graph Density", fontsize=14)
    plt.ylabel("Number of Operations", fontsize=14)
    plt.title("Backtracking Algorithm: Operations vs Graph Density", fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()

    plt.savefig("Operations_vs_Graph_Density.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    benchmark()
