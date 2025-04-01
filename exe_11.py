import time

def print_board(board):
    for row in board:
        print(" ".join(f"{cell:2d}" for cell in row))
    print()

# Abordagem por força bruta (backtracking)
def knight_tour_brute(n, start_x=0, start_y=0):
    board = [[-1] * n for _ in range(n)]
    moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]
    board[start_x][start_y] = 0

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def solve(x, y, movei):
        if movei == n * n:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                board[nx][ny] = movei
                if solve(nx, ny, movei + 1):
                    return True
                board[nx][ny] = -1  # backtracking
        return False

    if solve(start_x, start_y, 1):
        return board
    return None

# Abordagem com heurística de Warnsdorff
def knight_tour_warnsdorff(n, start_x=0, start_y=0):
    board = [[-1] * n for _ in range(n)]
    moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)]
    board[start_x][start_y] = 0

    def count_moves(x, y):
        count = 0
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                count += 1
        return count

    def solve(x, y, movei):
        if movei == n * n:
            return True
        next_moves = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                next_moves.append((count_moves(nx, ny), dx, dy))
        next_moves.sort(key=lambda x: x[0])  # menor grau primeiro
        for _, dx, dy in next_moves:
            nx, ny = x + dx, y + dy
            board[nx][ny] = movei
            if solve(nx, ny, movei + 1):
                return True
            board[nx][ny] = -1
        return False

    if solve(start_x, start_y, 1):
        return board
    return None

# Teste para diferentes tamanhos de tabuleiro
if __name__ == "__main__":
    sizes = [5, 8, 10]
    for n in sizes:
        print(f"--- Tabuleiro {n}x{n} - Força Bruta ---")
        start_time = time.time()
        board = knight_tour_brute(n)
        elapsed = time.time() - start_time
        if board:
            print_board(board)
        else:
            print("Nenhuma solução encontrada.")
        print("Tempo de execução: {:.4f} s".format(elapsed))

        print(f"--- Tabuleiro {n}x{n} - Heurística (Warnsdorff) ---")
        start_time = time.time()
        board = knight_tour_warnsdorff(n)
        elapsed = time.time() - start_time
        if board:
            print_board(board)
        else:
            print("Nenhuma solução encontrada.")
        print("Tempo de execução: {:.4f} s".format(elapsed))
