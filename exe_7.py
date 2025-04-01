import math

def floyd_warshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    vertices = ["A", "B", "C", "D", "E", "F"]
    n = len(vertices)
    INF = math.inf

    # Inicializa a matriz com INF e diagonal zero
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    # Definição das arestas (tempos em minutos)
    edges = [
        ("A", "B", 5),
        ("A", "C", 10),
        ("B", "C", 3),
        ("B", "D", 8),
        ("C", "D", 2),
        ("C", "E", 7),
        ("D", "E", 4),
        ("D", "F", 6),
        ("E", "F", 5)
    ]
    idx = {v: i for i, v in enumerate(vertices)}
    for u, v, w in edges:
        dist[idx[u]][idx[v]] = w

    # Calcula os menores tempos entre todos os pares de bairros
    shortest = floyd_warshall(dist)

    print("Matriz dos menores tempos de deslocamento (min):")
    for i in range(n):
        row = [f"{shortest[i][j]:.0f}" if shortest[i][j] != INF else "INF" for j in range(n)]
        print(f"{vertices[i]}: " + "\t".join(row))

    # Tempo mínimo de A até F
    time_A_F = shortest[idx["A"]][idx["F"]]
    print("\nTempo mínimo de A até F:", time_A_F, "minutos")
