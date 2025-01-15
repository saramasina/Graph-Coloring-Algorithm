import networkx as nx

def dsatur_coloring(graph):
    # Inițializăm culorile nodurilor
    coloring = {}
    saturation = {node: 0 for node in graph.nodes()}
    degrees = {node: len(list(graph.neighbors(node))) for node in graph.nodes()}

    # Sortăm nodurile după gradul lor
    sorted_nodes = sorted(degrees.keys(), key=lambda x: (-degrees[x], x))

    while sorted_nodes:
        # Alegem nodul cu saturația maximă și gradul maxim
        current_node = max(sorted_nodes, key=lambda x: (saturation[x], degrees[x]))

        # Găsim prima culoare disponibilă
        neighbor_colors = {coloring[neighbor] for neighbor in graph.neighbors(current_node) if neighbor in coloring}
        color = 0
        while color in neighbor_colors:
            color += 1

        # Atribuim culoarea și actualizăm saturația vecinilor
        coloring[current_node] = color
        sorted_nodes.remove(current_node)
        for neighbor in graph.neighbors(current_node):
            if neighbor not in coloring:
                saturation[neighbor] += 1

    return coloring
