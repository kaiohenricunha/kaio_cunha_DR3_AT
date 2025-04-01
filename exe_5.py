from collections import deque

# Representação do grafo como lista de adjacência
metro = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "E"],
    "E": ["B", "D", "F"],
    "F": ["C", "E"]
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            order += dfs(graph, neighbor, visited)
    return order

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# Exemplo de uso:
if __name__ == "__main__":
    print("DFS a partir da estação A:", dfs(metro, "A"))
    print("BFS a partir da estação A:", bfs(metro, "A"))
