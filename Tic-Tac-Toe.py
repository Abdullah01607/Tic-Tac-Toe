
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in win_positions:
        if (
            board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player
        ):
            return True

    return False


def is_draw(board):
    return " " not in board


def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:

        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter position (1-9): "))

            if move < 1 or move > 9:
                print("Invalid position! Try again.")
                continue

            if board[move - 1] != " ":
                print("Position already taken!")
                continue

            board[move - 1] = current_player

        except ValueError:
            print("Please enter a number!")
            continue

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# Main Menu Loop
while True:

    print("\n===== TIC TAC TOE =====")
    print("1. Play Game")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        while True:
            play_game()

            rematch = input("\nDo you want a rematch? (y/n): ").lower()

            if rematch != "y":
                print("Returning to main menu...")
                break

    elif choice == "2":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice! Try again.")