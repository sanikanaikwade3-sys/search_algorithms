
from collections import deque
import time


# Initial and goal states
initial_state = (1, 2, 3,
                 4, 0, 6,
                 7, 5, 8)

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


# Generate all possible next states
def get_neighbors(state):
    neighbors = []

    # Find the blank position
    blank_position = state.index(0)

    row = blank_position // 3
    col = blank_position % 3

    # Possible movements of blank space
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        # Check whether the new position is inside the puzzle
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_position = new_row * 3 + new_col

            # Create a new state
            new_state = list(state)

            # Swap blank with the new position
            new_state[blank_position], new_state[new_position] = \
                new_state[new_position], new_state[blank_position]

            neighbors.append(tuple(new_state))

    return neighbors


# BFS algorithm
def bfs(initial, goal):

    queue = deque([(initial, [])])
    visited = {initial}
    nodes_expanded = 0

    while queue:

        current_state, path = queue.popleft()
        nodes_expanded += 1

        # Check whether goal is reached
        if current_state == goal:
            return path, nodes_expanded

        # Generate next states
        for neighbor in get_neighbors(current_state):

            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None, nodes_expanded


# Run BFS and measure time
start_time = time.perf_counter()
solution, nodes_expanded = bfs(initial_state, goal_state)
end_time = time.perf_counter()
execution_time = end_time - start_time


# Display results
print("===== BFS RESULTS =====")

if solution is not None:
    print("Solution found!")
    print("Number of moves:", len(solution))
    print("Nodes expanded:", nodes_expanded)
    print("Execution time:", execution_time, "seconds")

else:

    print("No solution found.")


