import time


def forward_check(board, row, n, domains, stats):

    # All queens placed
    if row == n:
        return True

    # Try each column in the current row
    for col in domains[row]:

        stats["assignments"] += 1

        # Check whether placing queen is safe
        safe = True

        for previous_row in range(row):
            previous_col = board[previous_row]

            # Same column
            if previous_col == col:
                safe = False
                break

            # Same diagonal
            if abs(previous_row - row) == abs(previous_col - col):
                safe = False
                break

        if not safe:
            continue

        # Place queen
        board[row] = col

        # Make a copy of domains
        new_domains = [d.copy() for d in domains]

        # Forward checking
        for future_row in range(row + 1, n):

            new_domains[future_row] = [
                future_col
                for future_col in new_domains[future_row]
                if future_col != col
                and abs(future_row - row) != abs(future_col - col)
            ]

        # Check whether any future row has no available column
        valid = True

        for future_row in range(row + 1, n):
            if len(new_domains[future_row]) == 0:
                valid = False
                break

        # Continue if all future domains are valid
        if valid:
            if forward_check(
                board,
                row + 1,
                n,
                new_domains,
                stats
            ):
                return True

        # Backtrack
        board[row] = -1
        stats["backtracks"] += 1

    return False


# --------------------------------
# Main Program
# --------------------------------

n = 4

board = [-1] * n

# Initial domain:
# Every row can initially use every column
domains = [list(range(n)) for _ in range(n)]

stats = {
    "assignments": 0,
    "backtracks": 0
}

start_time = time.perf_counter()

solution_found = forward_check(
    board,
    0,
    n,
    domains,
    stats
)

end_time = time.perf_counter()

execution_time = end_time - start_time


# --------------------------------
# Display Result
# --------------------------------

if solution_found:

    print("Solution Found:\n")

    for row in range(n):

        for col in range(n):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

    print("\nAssignments:", stats["assignments"])
    print("Backtracks:", stats["backtracks"])
    print("Execution Time:", execution_time, "seconds")

else:

    print("No solution found.")