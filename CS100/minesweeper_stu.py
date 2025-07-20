# Minesweeper Starter Template (Student Version)

import random

def create_board(size, num_bombs):
    # TODO: Create a size x size board filled with ' '
    board = [[' ' for _ in range(size)] for _ in range(size)]
    bombs = 0
    while:
    # TODO: Randomly place '*' bombs on the board (num_bombs of them)
    pass

def count_bombs(board, row, col):
    # TODO: Count the number of bombs around a given cell (8 neighbors)
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(_____):
    pass

def add_numbers(board):
    # TODO: For each cell that is not a bomb, count surrounding bombs and fill it in
    size = len(board)
    pass

def create_hidden_board(size):
    # TODO: Create a board of same size with all cells as '■' (or other hidden marker)
    pass

def print_board(board):
    print("   " + " ".join([str(i) for i in range(len(board))]))
    print("  " + "-" * (len(board) * 2))
    for idx, row in enumerate(board):
        print(f"{idx}| " + " ".join(row))
    pass

def reveal_cell(board, hidden_board, row, col):
    # TODO: Reveal the cell on the hidden board
    # If it's a bomb, return False (game over). Else, update and return True.
    pass

def play_game(size=5, num_bombs=3):
    board = create_board(size, num_bombs)
    add_numbers(board)
    hidden = create_hidden_board(size)
    revealed = 0
    total_safe = size * size - num_bombs

    while True:
        print_board(hidden)
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if not (0 <= row < size and 0 <= col < size):
            print("Out of range. Try again.")
            continue

        if hidden[row][col] != '■':
            print("Cell already revealed. Choose another.")
            continue

        if not reveal_cell(board, hidden, row, col):
            print_board(board)
            print("💥 You hit a bomb! Game over.")
            break

        revealed += 1
        if revealed == total_safe:
            print_board(hidden)
            print("🎉 You win!")
            break

# Uncomment this line when you're ready to test your game!
# play_game()
