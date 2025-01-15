import os
import time
import networkx as nx
import matplotlib.pyplot as plt  # Import corect pentru plotare
from dsatur import dsatur_coloring

# Funcție pentru citirea unui fișier de graf
def load_graph(filepath):
    return nx.read_edgelist(filepath, nodetype=int)

# Funcție pentru rularea DSATUR și măsurarea timpului
def run_dsatur(graph):
    start_time = time.time()
    coloring = dsatur_coloring(graph)  # Aplicăm algoritmul DSATUR
    end_time = time.time()
    return end_time - start_time  # Returnează doar timpul de execuție

# Directoarele de intrare
input_dir = "input"
categories = ["bipartite", "complete", "HC", "planar", "random", "sparse"]

# Colectăm datele pentru grafic
execution_times = []  # Timpurile de execuție
edge_counts = []  # Numărul de muchii

# Iterăm prin fiecare categorie și fișier
for category in categories:
    category_path = os.path.join(input_dir, category)

    for filename in os.listdir(category_path):
        if filename.endswith(".edgelist"):
            filepath = os.path.join(category_path, filename)
            print(f"Processing {filepath}...")

            # Încărcăm graful
            graph = load_graph(filepath)

            # Obținem numărul de muchii al grafului
            edge_count = graph.number_of_edges()
            edge_counts.append(edge_count)

            # Rulăm DSATUR și obținem timpul de execuție
            dsatur_time = run_dsatur(graph)
            execution_times.append(dsatur_time)

# Generăm graficul de tip scatter
plt.figure(figsize=(10, 6))

# Adăugăm punctele în grafic
plt.scatter(edge_counts, execution_times, color='skyblue', edgecolor='black')

# Personalizare grafic
plt.xlabel("Number of Edges", fontsize=14)
plt.ylabel("Execution Time (s)", fontsize=14)
plt.title("DSATUR Algorithm Execution Time vs Number of Edges", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()

# Salvăm figura
plt.savefig("Execution_Time_vs_Number_of_Edges.png", dpi=300)  # DPI mai mare pentru o calitate mai bună
plt.show()
