import time

nodes_expanded = 0
backtracks = 0


def is_safe(board, row, col, n):

    # Check previous rows
    for previous_row in range(row):

        previous_col = board[previous_row]

        # Same column
        if previous_col == col:
            return False

        # Same diagonal
        if abs(previous_row - row) == abs(previous_col - col):
            return False

    return True


def solve_nqueens(board, row, n):

    global nodes_expanded
    global backtracks

    # All queens placed
    if row == n:
        return True

    # Try every column
    for col in range(n):

        nodes_expanded += 1

        if is_safe(board, row, col, n):

            board[row] = col

            if solve_nqueens(board, row + 1, n):
                return True

            # Backtrack
            board[row] = -1
            backtracks += 1

    return False


def print_board(board, n):

    for row in range(n):

        for col in range(n):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# Problem size
n = 4

board = [-1] * n

# Measure time
start_time = time.perf_counter()

solution_found = solve_nqueens(board, 0, n)

end_time = time.perf_counter()

execution_time = end_time - start_time


# Display results
print("===== N-QUEENS BACKTRACKING =====")

if solution_found:
    print("Solution found!")
    print_board(board, n)
else:
    print("No solution found.")

print("Nodes expanded:", nodes_expanded)
print("Backtracks:", backtracks)
print("Execution time:", execution_time, "seconds")