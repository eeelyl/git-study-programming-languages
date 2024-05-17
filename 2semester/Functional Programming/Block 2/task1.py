def is_safe(board, row, col, n):
    # Проверка вертикали
    for i in range(row):
        if board[i] == col:
            return False

    # Проверка диагонали (\)
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Проверка диагонали (/)
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i] == j:
            return False

    return True


def solve_n_queens(board, row, n):
    if row == n:
        yield list(board)
    else:
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                yield from solve_n_queens(board, row + 1, n)
                board[row] = -1  # Сброс позиции королевы


def n_queens_generator(n):
    board = [-1] * n
    yield from solve_n_queens(board, 0, n)


# Пример использования
n = 8
solutions = n_queens_generator(n)
for solution in solutions:
    print(solution)
