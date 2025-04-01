import math

# Representação usando Matriz de Adjacência
class GraphMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.size = len(vertices)
        self.index = {v: i for i, v in enumerate(vertices)}
        # Inicializa com infinito (sem conexão) e 0 na diagonal
        self.matrix = [[0 if i == j else math.inf for j in range(self.size)] for i in range(self.size)]

    def add_edge(self, u, v, weight):
        i, j = self.index[u], self.index[v]
        self.matrix[i][j] = weight
        self.matrix[j][i] = weight  # grafo não direcionado

    def display(self):
        print("Matriz de Adjacência:")
        for row in self.matrix:
            print(row)


# Representação usando Lista de Adjacência
class GraphList:
    def __init__(self, vertices):
        self.graph = {v: [] for v in vertices}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # grafo não direcionado

    def display(self):
        print("Lista de Adjacência:")
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")


# Exemplo de uso:
if __name__ == "__main__":
    vertices = ["A", "B", "C", "D", "E", "F"]
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 3),
        ("D", "F", 6),
        ("E", "F", 1)
    ]

    # Utilizando Matriz de Adjacência
    gm = GraphMatrix(vertices)
    for u, v, w in edges:
        gm.add_edge(u, v, w)
    gm.display()
    print()

    # Utilizando Lista de Adjacência
    gl = GraphList(vertices)
    for u, v, w in edges:
        gl.add_edge(u, v, w)
    gl.display()
