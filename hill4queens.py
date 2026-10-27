
def cost(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing(state):
    current = state[:]
    current_cost = cost(current)

    print("Initial state:", current)
    print("Initial cost:", current_cost)

    while current_cost > 0:
        best = current[:]
        best_cost = current_cost

        print("\nCurrent state:", current)
        print("Current cost:", current_cost)

        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                neighbor = current[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbor_cost = cost(neighbor)

                print("\nSwap columns", i, "and", j)
                print("Neighbor:", neighbor)
                print("Neighbor cost:", neighbor_cost)

                if neighbor_cost < best_cost:
                    best = neighbor
                    best_cost = neighbor_cost

        if best_cost >= current_cost:
            print("\nLocal minimum reached!")
            break

        current = best
        current_cost = best_cost

        print("\nBest neighbor selected:", current)

    print("\nFinal state:", current)
    print("Final cost:", current_cost)

    if current_cost == 0:
        print("Solution found!")
    else:
        print("Solution not found!")


state = list(map(int, input(
    "Enter the row positions of queens: "
).split()))

if sorted(state) != list(range(len(state))):
    print("Enter each row number from 0 to N-1 exactly once.")
else:
    hill_climbing(state)
