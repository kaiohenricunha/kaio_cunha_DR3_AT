import heapq

def dijkstra(graph, start, end):
    distances = {v: float('inf') for v in graph}
    previous = {v: None for v in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        cur_dist, cur_vertex = heapq.heappop(queue)
        if cur_vertex == end:
            break
        if cur_dist > distances[cur_vertex]:
            continue
        for neighbor, weight in graph[cur_vertex].items():
            distance = cur_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = cur_vertex
                heapq.heappush(queue, (distance, neighbor))
                
    # Reconstrução da rota
    path = []
    curr = end
    while curr:
        path.append(curr)
        curr = previous[curr]
    path.reverse()
    return path, distances[end]

# Exemplo de uso:
if __name__ == "__main__":
    # Grafo ponderado representado como lista de adjacência
    graph = {
        "CD": {"A": 4, "B": 2},
        "A": {"C": 5, "D": 10},
        "B": {"A": 3, "D": 8},
        "C": {"D": 2, "E": 4},
        "D": {"E": 6, "F": 5},
        "E": {"F": 3},
        "F": {}
    }
    
    route, cost = dijkstra(graph, "CD", "F")
    print("Rota ótima:", route)
    print("Custo total:", cost, "km")
