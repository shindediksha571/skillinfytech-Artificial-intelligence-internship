import math

# Create board
board = [" " for _ in range(9)]

# Display board
def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-" * 9)
    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Main Game Loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print("Positions:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

    while True:
        print_board()

        # Player Move
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Enter a valid number!")
            continue

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("You Win!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

        # AI Move
        ai_move()

        if check_winner("O"):
            print_board()
            print("AI Wins!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

play_game()
