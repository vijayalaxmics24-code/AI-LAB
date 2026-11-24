import random
import math

N = 8

def cost(board):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def display_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def simulated_annealing():
    # Random initial state with unique rows and columns
    current = random.sample(range(N), N)

    print("Initial State:", [x + 1 for x in current])
    print("Initial Conflicts:", cost(current))
    display_board(current)

    T = 100.0
    cooling_rate = 0.99
    min_temperature = 0.001

    while T > min_temperature:
        if cost(current) == 0:
            break

        # Generate a neighbour by swapping two queen rows
        next_state = current[:]
        i, j = random.sample(range(N), 2)
        next_state[i], next_state[j] = next_state[j], next_state[i]

        delta_E = cost(next_state) - cost(current)

        # Accept better states or probabilistically accept worse states
        if delta_E <= 0 or random.random() < math.exp(-delta_E / T):
            current = next_state

        T *= cooling_rate

    print("\nFinal State:", [x + 1 for x in current])
    print("Final Conflicts:", cost(current))
    display_board(current)


simulated_annealing()
