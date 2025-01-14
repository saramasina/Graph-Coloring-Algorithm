import networkx as nx
import os
import random

def generate_bipartite_graph(nodes, edges):
    # Împărțim nodurile în două seturi
    set1 = range(nodes // 2)
    set2 = range(nodes // 2, nodes)
    
    # Cream un graf bipartit gol
    B = nx.Graph()
    B.add_nodes_from(set1, bipartite=0)  # Primul set
    B.add_nodes_from(set2, bipartite=1)  # Al doilea set
    
    # Generăm muchii între seturi
    possible_edges = [(u, v) for u in set1 for v in set2]
    selected_edges = random.sample(possible_edges, edges)  # Alegem `edges` muchii aleatorii
    B.add_edges_from(selected_edges)
    
    return B

def generate_hard_to_color_graph(n, p, clique_size):
    # Graful aleatoriu
    G = nx.erdos_renyi_graph(n, p)

    # Adăugăm un clique mare
    clique = nx.complete_graph(clique_size)
    G = nx.disjoint_union(G, clique)

    # Conectăm clique-ul cu graful aleatoriu
    for _ in range(clique_size):
        G.add_edge(random.choice(range(n)), n + random.choice(range(clique_size)))

    return G

for i in range(7):
        # Generăm numărul aleatoriu de noduri și muchii
        num_nodes = random.randint(1, 60)
        num_edges = random.randint(1, 1000)  # Maximum edges for the graph

        # Creăm graful aleatoriu
        graph = nx.gnm_random_graph(num_nodes, num_edges)

        # Salvăm graful în format edge list
        file_path = os.path.join("C:/Users/Sara/Graph-Coloring-Algorithm/input/random", f"random_graph{i+1}.edgelist")
        nx.write_edgelist(graph, file_path)
        print(f"Graful {i+1} a fost salvat în {file_path}")

for i in range(7):
        # Generăm numărul aleatoriu de noduri și muchii
        num_nodes = random.randint(1, 60)

        # Creăm graful aleatoriu
        graph = nx.complete_graph(num_nodes)

        # Salvăm graful în format edge list
        file_path = os.path.join("C:/Users/Sara/Graph-Coloring-Algorithm/input/complete", f"complete_graph{i+1}.edgelist")
        nx.write_edgelist(graph, file_path)
        print(f"Graful {i+1} a fost salvat în {file_path}")

for i in range(7):
        # Generăm numărul aleatoriu de noduri și muchii
        num_nodes = random.randint(1, 60)

        # Creăm graful aleatoriu
        graph =G = G = nx.erdos_renyi_graph(num_nodes, p=0.05)  # 5% șansă ca o muchie să existe

        # Salvăm graful în format edge list
        file_path = os.path.join("C:/Users/Sara/Graph-Coloring-Algorithm/input/sparse", f"sparse_graph{i+1}.edgelist")
        nx.write_edgelist(graph, file_path)
        print(f"Graful {i+1} a fost salvat în {file_path}")

for i in range(13):
        # Generăm numărul aleatoriu de noduri și muchii
        num_nodes = random.randint(1, 15)

        # Creăm graful aleatoriu
        graph = nx.mycielski_graph(num_nodes)

        # Salvăm graful în format edge list
        file_path = os.path.join("C:/Users/Sara/Graph-Coloring-Algorithm/input/SHC", f"SHC_graph{i+1}.edgelist")
        nx.write_edgelist(graph, file_path)
        print(f"Graful {i+1} a fost salvat în {file_path}")

for i in range(13):
        # Generăm numărul aleatoriu de noduri și muchii
        num_nodes = random.randint(1, 20)

        # Creăm graful aleatoriu
        graph = generate_hard_to_color_graph(num_nodes, 0.2, 6)

        # Salvăm graful în format edge list
        file_path = os.path.join("C:/Users/Sara/Graph-Coloring-Algorithm/input/HC", f"HC_graph{i+1}.edgelist")
        nx.write_edgelist(graph, file_path)
        print(f"Graful {i+1} a fost salvat în {file_path}")
       
