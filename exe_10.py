import heapq

def prim_mst(graph):
    """
    Calcula a Árvore Geradora Mínima (MST) usando o algoritmo de Prim.
    graph: dicionário onde cada chave é uma cidade e o valor é uma lista de tuplas (cidade vizinha, custo).
    Retorna uma lista de arestas selecionadas e o custo total.
    """
    start = next(iter(graph))  # pega uma cidade arbitrária para iniciar
    visited = {start}
    edges = [(cost, start, neighbor) for neighbor, cost in graph[start]]
    heapq.heapify(edges)
    mst = []
    total_cost = 0

    while edges and len(visited) < len(graph):
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            total_cost += cost
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst, total_cost

# Exemplo de uso:
if __name__ == "__main__":
    # Representação do grafo: cada cidade e suas conexões com respectivos custos
    graph = {
        "A": [("B", 4), ("C", 3)],
        "B": [("A", 4), ("C", 1), ("D", 2)],
        "C": [("A", 3), ("B", 1), ("D", 4), ("E", 5)],
        "D": [("B", 2), ("C", 4), ("E", 1)],
        "E": [("C", 5), ("D", 1)]
    }
    
    mst, total_cost = prim_mst(graph)
    print("MST:", mst)
    print("Custo Total:", total_cost)
