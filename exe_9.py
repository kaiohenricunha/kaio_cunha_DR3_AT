def greedy_set_cover(uncovered, warehouses):
    """
    uncovered: conjunto de lojas que precisam ser cobertas
    warehouses: dicionário onde a chave é o identificador do armazém
                e o valor é um conjunto de lojas que ele cobre
    Retorna uma lista dos armazéns selecionados.
    """
    selected = []
    while uncovered:
        best_warehouse = None
        covered_stores = set()
        # Seleciona o armazém que cobre o maior número de lojas ainda não atendidas
        for wh, stores in warehouses.items():
            covered = uncovered & stores
            if len(covered) > len(covered_stores):
                best_warehouse = wh
                covered_stores = covered
        if not best_warehouse:
            break  # Caso não haja mais armazéns que cubram as lojas restantes
        selected.append(best_warehouse)
        uncovered -= covered_stores
    return selected

# Exemplo de uso:
if __name__ == "__main__":
    # Definindo os armazéns candidatos e as lojas que cada um pode atender
    warehouses = {
        "W1": {"L1", "L2", "L3"},
        "W2": {"L2", "L4"},
        "W3": {"L3", "L4", "L5"},
        "W4": {"L5", "L6"},
        "W5": {"L1", "L6", "L7"}
    }
    
    # Conjunto de todas as lojas que precisam ser cobertas
    all_stores = {"L1", "L2", "L3", "L4", "L5", "L6", "L7"}
    
    selected = greedy_set_cover(all_stores.copy(), warehouses)
    print("Armazéns selecionados:", selected)
