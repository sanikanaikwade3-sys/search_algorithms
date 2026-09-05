import heapq
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
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
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


# Manhattan Distance heuristic
def heuristic(state, goal):

    distance = 0

    for i in range(9):

        tile = state[i]

        if tile == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        goal_position = goal.index(tile)

        goal_row = goal_position // 3
        goal_col = goal_position % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# A* Search
def astar(initial, goal):

    # Priority queue
    # (f, g, state, path)
    priority_queue = []

    g = 0
    h = heuristic(initial, goal)
    f = g + h

    heapq.heappush(
        priority_queue,
        (f, g, initial, [])
    )

    visited = set()

    nodes_expanded = 0

    while priority_queue:

        f, g, current_state, path = heapq.heappop(priority_queue)

        if current_state in visited:
            continue

        visited.add(current_state)

        nodes_expanded += 1

        # Goal test
        if current_state == goal:
            return path, nodes_expanded

        # Generate neighbors
        for neighbor in get_neighbors(current_state):

            if neighbor not in visited:

                new_g = g + 1

                new_h = heuristic(neighbor, goal)

                new_f = new_g + new_h

                new_path = path + [neighbor]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, new_path)
                )

    return None, nodes_expanded


# Measure execution time
start_time = time.perf_counter()

solution, nodes_expanded = astar(initial_state, goal_state)

end_time = time.perf_counter()

execution_time = end_time - start_time


# Display results
print("===== A* SEARCH RESULTS =====")

if solution is not None:

    print("Solution found!")
    print("Number of moves:", len(solution))
    print("Nodes expanded:", nodes_expanded)
    print("Execution time:", execution_time, "seconds")

else:

    print("No solution found.")