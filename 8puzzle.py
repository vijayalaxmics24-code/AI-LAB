
def solve(state, goal, limit, path, visited):
    if state == goal:
        return path
    if limit == 0:
        return None

    visited.add(tuple(state))
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

        if tuple(new_state) not in visited:
            result = solve(
                new_state, goal, limit - 1,
                path + [new_state], visited
            )
            if result:
                return result
    return None


def dfs(start, goal):
    return solve(start, goal, 30, [start], set())


def ids(start, goal):
    for depth in range(50):
        result = solve(start, goal, depth, [start], set())
        if result:
            return result
    return None


def display(path):
    if path:
        print("Number of moves:", len(path) - 1)
        for i, state in enumerate(path):
            print("\nStep", i)
            for j in range(0, 9, 3):
                print(tuple(state[j:j+3]))
    else:
        print("No solution found!")


print("8 PUZZLE USING DFS AND IDS")

start = list(map(int, input(
    "Enter Initial State (use 0 for blank): "
).split()))

goal = list(map(int, input(
    "Enter Goal State (use 0 for blank): "
).split()))

print("\nInitial State:")
for i in range(0, 9, 3):
    print(tuple(start[i:i+3]))

print("\nGoal State:")
for i in range(0, 9, 3):
    print(tuple(goal[i:i+3]))

print("\nOUTPUT FOR DFS")
display(dfs(start, goal))

print("\nOUTPUT FOR IDS")
display(ids(start, goal))
