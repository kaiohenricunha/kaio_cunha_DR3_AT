import math, random, time

# Função para calcular o custo total de uma rota (assumindo que a rota começa e termina na cidade 0)
def route_cost(route, distance):
    cost = 0
    prev = 0
    for city in route:
        cost += distance[prev][city]
        prev = city
    return cost + distance[prev][0]

# 1. Solução Exata: Held-Karp (DP com bitmask)
def tsp_exact(distance):
    n = len(distance)
    dp = {}     # dp[(mask, i)] = custo mínimo para atingir i com o conjunto mask visitado
    parent = {} # Para reconstruir o caminho
    dp[(1, 0)] = 0  # Começa na cidade 0; mask=1 indica que 0 foi visitada

    for mask in range(1, 1 << n):
        for i in range(n):
            if mask & (1 << i) and (mask, i) in dp:
                for j in range(n):
                    if mask & (1 << j) == 0:
                        next_mask = mask | (1 << j)
                        new_cost = dp[(mask, i)] + distance[i][j]
                        if (next_mask, j) not in dp or new_cost < dp[(next_mask, j)]:
                            dp[(next_mask, j)] = new_cost
                            parent[(next_mask, j)] = i

    final_mask = (1 << n) - 1
    best_cost = float('inf')
    last = None
    for i in range(1, n):
        cost = dp.get((final_mask, i), float('inf')) + distance[i][0]
        if cost < best_cost:
            best_cost = cost
            last = i

    # Reconstrução do caminho
    path = [0]
    mask = final_mask
    cur = last
    rev_path = [cur]
    while mask != 1:
        prev = parent[(mask, cur)]
        rev_path.append(prev)
        mask = mask ^ (1 << cur)
        cur = prev
    rev_path.reverse()
    path = rev_path + [0]
    return best_cost, path

# 2. Heurística Gulosa: Vizinho Mais Próximo
def tsp_greedy(distance):
    n = len(distance)
    current = 0
    visited = [False] * n
    visited[0] = True
    path = [0]
    total_cost = 0
    for _ in range(n - 1):
        next_city = None
        best = float('inf')
        for j in range(n):
            if not visited[j] and distance[current][j] < best:
                best = distance[current][j]
                next_city = j
        path.append(next_city)
        visited[next_city] = True
        total_cost += best
        current = next_city
    total_cost += distance[current][0]
    path.append(0)
    return total_cost, path

# 3. Algoritmo Genético para TSP
def tsp_genetic(distance, population_size=100, generations=500, mutation_rate=0.1):
    n = len(distance)
    # Cada indivíduo é uma permutação das cidades (exceto a 0, que é fixa no início e fim)
    population = [random.sample(range(1, n), n - 1) for _ in range(population_size)]

    def fitness(route):
        return 1.0 / route_cost(route, distance)

    for _ in range(generations):
        # Ordena a população de acordo com o custo (menor custo primeiro)
        population.sort(key=lambda route: route_cost(route, distance))
        new_population = population[:population_size // 10]  # elitismo: top 10%

        while len(new_population) < population_size:
            parent1 = random.choice(population[:population_size // 2])
            parent2 = random.choice(population[:population_size // 2])
            # Crossover por ordem: escolhe um segmento de parent1 e preenche com os de parent2 na ordem
            cut1 = random.randint(0, n - 2)
            cut2 = random.randint(cut1, n - 2)
            child = parent1[cut1:cut2]
            child += [city for city in parent2 if city not in child]
            # Mutação: troca dois elementos
            if random.random() < mutation_rate:
                i, j = random.sample(range(n - 1), 2)
                child[i], child[j] = child[j], child[i]
            new_population.append(child)
        population = new_population

    best_route = min(population, key=lambda route: route_cost(route, distance))
    best_cost = route_cost(best_route, distance)
    # Inclui a cidade 0 no início e no fim
    return best_cost, [0] + best_route + [0]

# Exemplo de uso e comparação
if __name__ == "__main__":
    # Matriz de distâncias para 5 cidades (simétrica)
    distance = [
        [0, 10, 15, 20, 10],
        [10, 0, 35, 25, 15],
        [15, 35, 0, 30, 20],
        [20, 25, 30, 0, 15],
        [10, 15, 20, 15, 0]
    ]

    print("=== TSP Exato (Held-Karp) ===")
    start = time.time()
    cost_exact, path_exact = tsp_exact(distance)
    elapsed = time.time() - start
    print("Custo:", cost_exact)
    print("Rota :", path_exact)
    print("Tempo de execução: {:.4f} s".format(elapsed))
    print()

    print("=== TSP Guloso (Vizinho Mais Próximo) ===")
    start = time.time()
    cost_greedy, path_greedy = tsp_greedy(distance)
    elapsed = time.time() - start
    print("Custo:", cost_greedy)
    print("Rota :", path_greedy)
    print("Tempo de execução: {:.4f} s".format(elapsed))
    print()

    print("=== TSP Algoritmo Genético ===")
    start = time.time()
    cost_gen, path_gen = tsp_genetic(distance)
    elapsed = time.time() - start
    print("Custo:", cost_gen)
    print("Rota :", path_gen)
    print("Tempo de execução: {:.4f} s".format(elapsed))
