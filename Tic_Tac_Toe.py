# Tic Tac Toe Game in Python

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Checks if the current player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True

    # Check diagonals
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True

    return False


def check_draw(board):
    """Checks if the game is a draw."""
    return all([cell != ' ' for row in board for cell in row])


def make_move(board, player):
    """Handles player's move input and updates the board."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1

            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("This position is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 1 and 3.")


def tic_tac_toe():
    """Main function to start the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        make_move(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    tic_tac_toe()
