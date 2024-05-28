def is_valid_move(x, y, board, n):
    """Check if the move is valid and the cell has not been visited."""
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def knight_tour_generator(n):
    """Generator to solve the Knight's Tour problem."""
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board = [[-1 for _ in range(n)] for _ in range(n)]

    x, y = 0, 0
    board[x][y] = 0
    yield (x, y, board)

    def solve_knight_tour(x, y, move_count):
        """Utility function to solve the Knight's Tour problem."""
        if move_count == n * n:
            return True

        for i in range(8):
            next_x, next_y = x + move_x[i], y + move_y[i]
            if is_valid_move(next_x, next_y, board, n):
                board[next_x][next_y] = move_count
                yield (next_x, next_y, board)
                if (yield from solve_knight_tour(next_x, next_y, move_count + 1)):
                    return True
                board[next_x][next_y] = -1

        return False

    yield from solve_knight_tour(x, y, 1)


n = 5
generator = knight_tour_generator(n)

for move in generator:
    x, y, board = move
    print(f"Move to: ({x}, {y})")
    for row in board:
        print(row)
    print()
