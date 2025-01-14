import time
import networkx as nx
import matplotlib.pyplot as plt

def recursive_largest_first(graph):
    # Sort vertices by degree in descending order
    nodes = sorted(graph.nodes(), key=lambda x: graph.degree(x), reverse=True)
    color_map = {}
    
    for node in nodes:
        used_colors = {color_map[neighbor] for neighbor in graph.neighbors(node) if neighbor in color_map}
        color_map[node] = next(color for color in range(len(graph)) if color not in used_colors)
    
    return color_map

# Generarea grafurilor de test
def generate_test_graphs():
    graphs = []
    for num_nodes in range(10, 101, 10):  # Grafuri cu 10, 20, ..., 100 noduri
        for edge_prob in [0.1, 0.25, 0.5, 0.75]:  # Densități diferite
            g = nx.erdos_renyi_graph(num_nodes, edge_prob)
            graphs.append((g, num_nodes, edge_prob))
    return graphs

# Măsurarea timpului de execuție
def measure_performance(graphs):
    results = []
    for graph, num_nodes, edge_prob in graphs:
        num_edges = graph.number_of_edges()
        start_time = time.time()
        recursive_largest_first(graph)
        elapsed_time = time.time() - start_time
        results.append((num_nodes, num_edges, edge_prob, elapsed_time))
    return results

# Generare grafice
def plot_results(results):
    num_nodes = [r[0] for r in results]
    num_edges = [r[1] for r in results]
    times = [r[3] for r in results]

    # Timp vs numărul de noduri
    plt.figure(figsize=(8, 6))
    plt.scatter(num_nodes, times, c='blue', label='Timp vs Noduri')
    plt.title('Timp de execuție vs Numărul de noduri')
    plt.xlabel('Numărul de noduri')
    plt.ylabel('Timp de execuție (s)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Timp vs numărul de muchii
    plt.figure(figsize=(8, 6))
    plt.scatter(num_edges, times, c='green', label='Timp vs Muchii')
    plt.title('Timp de execuție vs Numărul de muchii')
    plt.xlabel('Numărul de muchii')
    plt.ylabel('Timp de execuție (s)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Timp vs densitate
    densities = [2 * r[1] / (r[0] * (r[0] - 1)) for r in results]
    plt.figure(figsize=(8, 6))
    plt.scatter(densities, times, c='red', label='Timp vs Densitate')
    plt.title('Timp de execuție vs Densitatea grafului')
    plt.xlabel('Densitate')
    plt.ylabel('Timp de execuție (s)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Executare
graphs = generate_test_graphs()
results = measure_performance(graphs)
plot_results(results)
