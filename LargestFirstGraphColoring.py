import matplotlib.pyplot as plt
import networkx as nx

class Edge:
    def __init__(self, dest_id):
        self.dest_id = dest_id

    def get_dest_id(self):
        return self.dest_id


class Vertex:
    def __init__(self, vertex_id, name):
        self.vertex_id = vertex_id
        self.name = name
        self.color = -1  # Necolorat inițial
        self.num_connections = 0
        self.edges = []

    def get_id(self):
        return self.vertex_id

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_num_connections(self):
        return self.num_connections

    def add_edge(self, dest_id):
        self.edges.append(Edge(dest_id))
        self.num_connections += 1

    def get_edges(self):
        return self.edges

    def print_edge_list(self):
        edges = " -> ".join(str(edge.get_dest_id()) for edge in self.edges)
        print(f"[{edges}]")


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex):
        if all(v.get_id() != vertex.get_id() for v in self.vertices):
            self.vertices.append(vertex)

    def get_vertex(self, vertex_id):
        for vertex in self.vertices:
            if vertex.get_id() == vertex_id:
                return vertex
        return None

    def add_edge(self, source_id, dest_id):
        source = self.get_vertex(source_id)
        dest = self.get_vertex(dest_id)
        if source and dest:
            source.add_edge(dest_id)
            dest.add_edge(source_id)

    def print_graph(self):
        for vertex in self.vertices:
            print(f"{vertex.get_name()} ({vertex.get_id()}) --> ", end="")
            vertex.print_edge_list()

    def get_vertices(self):
        return self.vertices


def largest_first_coloring_algorithm(graph):
    vertices = sorted(graph.get_vertices(), key=lambda v: v.get_num_connections(), reverse=True)

    for vertex in vertices:
        used_colors = set()

        # Găsește culorile utilizate de vecini
        for edge in vertex.get_edges():
            neighbor = graph.get_vertex(edge.get_dest_id())
            if neighbor and neighbor.get_color() != -1:
                used_colors.add(neighbor.get_color())

        # Atribuie cea mai mică culoare disponibilă
        color = 0
        while color in used_colors:
            color += 1
        vertex.set_color(color)

    # Afișează rezultatul
    print("Culorile nodurilor:")
    for vertex in vertices:
        print(f"{vertex.get_name()} (ID: {vertex.get_id()}) -> Culoare: {vertex.get_color()}")

def visualize_colored_graph(graph):
    G = nx.Graph()

    # Adaugă noduri și muchii la obiectul NetworkX
    for vertex in graph.get_vertices():
        G.add_node(vertex.get_id(), label=vertex.get_name(), color=vertex.get_color())

    for vertex in graph.get_vertices():
        for edge in vertex.get_edges():
            G.add_edge(vertex.get_id(), edge.get_dest_id())

    # Extrage culorile nodurilor
    colors = [data['color'] for _, data in G.nodes(data=True)]
    labels = nx.get_node_attributes(G, 'label')

    # Desenare graf
    pos = nx.spring_layout(G)  # Poziționare automată
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=colors, cmap=plt.cm.rainbow, node_size=700, font_size=10)
    plt.show()


if __name__ == "__main__":
    graph = Graph()

    # Adaugă noduri
    graph.add_vertex(Vertex(0, "a"))
    graph.add_vertex(Vertex(1, "b"))
    graph.add_vertex(Vertex(2, "c"))
    graph.add_vertex(Vertex(3, "d"))
    graph.add_vertex(Vertex(4, "e"))
    graph.add_vertex(Vertex(5, "f"))
    graph.add_vertex(Vertex(6, "g"))
    graph.add_vertex(Vertex(7, "h"))

    # Adaugă muchii
    graph.add_edge(0, 4)
    graph.add_edge(0, 6)
    graph.add_edge(0, 5)
    graph.add_edge(1, 4)
    graph.add_edge(1, 7)
    graph.add_edge(2, 6)
    graph.add_edge(3, 5)
    graph.add_edge(3, 6)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)
    graph.add_edge(1, 2)

    # Afișează graful
    graph.print_graph()

    # Aplică algoritmul de colorare
    largest_first_coloring_algorithm(graph)

    # Vizualizează graful colorat
    visualize_colored_graph(graph)
