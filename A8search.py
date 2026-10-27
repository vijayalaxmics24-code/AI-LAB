
import heapq

def heuristic(state, goal):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])

def display(state):
    for i in range(0, 9, 3):
        print(tuple(state[i:i+3]))

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start, [start])]
    visited = {}

    while pq:
        f, g, state, path = heapq.heappop(pq)
        key = tuple(state)

        if key in visited and visited[key] <= g:
            continue
        visited[key] = g

        if state == goal:
            return path, g

        pos = state.index(0)
        row, col = divmod(pos, 3)

        for move in [-3, 3, -1, 1]:
            new_pos = pos + move

            if new_pos < 0 or new_pos >= 9:
                continue
            if move == -1 and col == 0:
                continue
            if move == 1 and col == 2:
                continue

            new_state = state.copy()
            new_state[pos], new_state[new_pos] = (
                new_state[new_pos], new_state[pos]
            )

            new_g = g + 1
            new_f = new_g + heuristic(new_state, goal)

            heapq.heappush(
                pq, (new_f, new_g, new_state, path + [new_state])
            )

    return None, 0


print("8-PUZZLE USING A*")
start = list(map(int, input(
    "Enter initial state (use 0 for blank): "
).split()))

goal = list(map(int, input(
    "Enter goal state (use 0 for blank): "
).split()))

print("\nInitial State:")
display(start)

print("\nGoal State:")
display(goal)

path, cost = astar(start, goal)

if path:
    print("\nA* USING MISPLACED TILES")
    print("Optimal cost:", cost)
    print("Total moves:", len(path) - 1)
    print("\nSolution Path:")

    for i, state in enumerate(path):
        print("\nStep", i)
        display(state)
else:
    print("No solution found!")