import time


# Initial state
initial_state = (1, 2, 3,
                 4, 0, 6,
                 7, 5, 8)

# Goal state
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


# Generate possible next states
def get_neighbors(state):

    neighbors = []

    blank_position = state.index(0)

    row = blank_position // 3
    col = blank_position % 3

    moves = [
        (-1, 0),   # Up
        (0, -1),   # Left
        (0, 1),    # Right
        (1, 0)     # Down
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            new_state = list(state)

            temp = new_state[blank_position]
            new_state[blank_position] = new_state[new_position]
            new_state[new_position] = temp

            neighbors.append(tuple(new_state))

    return neighbors


# DFS algorithm
def dfs(initial, goal):

    # Stack: Last In First Out
    stack = [(initial, [])]

    visited = set()
    visited.add(initial)

    nodes_expanded = 0

    while len(stack) > 0:

        current_state, path = stack.pop()

        nodes_expanded += 1

        # Check if goal is reached
        if current_state == goal:
            return path, nodes_expanded

        # Generate neighboring states
        neighbors = get_neighbors(current_state)

        for neighbor in neighbors:

            if neighbor not in visited:

                visited.add(neighbor)

                new_path = path + [neighbor]

                stack.append((neighbor, new_path))

    return None, nodes_expanded


# Measure execution time
start_time = time.perf_counter()

solution, nodes_expanded = dfs(initial_state, goal_state)

end_time = time.perf_counter()

execution_time = end_time - start_time


# Display results
print("===== DFS RESULTS =====")

if solution is not None:

    print("Solution found!")
    print("Number of moves:", len(solution))
    print("Nodes expanded:", nodes_expanded)
    print("Execution time:", execution_time, "seconds")

else:

    print("No solution found.")