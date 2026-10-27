

import random

board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('--+---+--')

def winner(p):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == p for i in line) for line in wins)

def computer_move():
    # Try to win first
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if winner('O'):
                return
            board[i] = ' '

    # Block the player from winning
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if winner('X'):
                board[i] = 'O'
                return
            board[i] = ' '

    # Otherwise, choose an available position
    available = [i for i in range(9) if board[i] == ' ']
    if available:
        board[random.choice(available)] = 'O'

while True:
    display()

    try:
        pos = int(input("Enter position (1-9): "))
    except ValueError:
        print("Enter a valid number!")
        continue

    if pos < 1 or pos > 9 or board[pos - 1] != ' ':
        print("Invalid position! Try again.")
        continue

    board[pos - 1] = 'X'

    if winner('X'):
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("It's a draw!")
        break

    computer_move()

    if winner('O'):
        display()
        print("Computer wins!")
        break

    if ' ' not in board:
        display()
        print("It's a draw!")
        break