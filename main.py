"""
A simple Tic-Tac-Toe game with a player and computer opponent.
The board is laid out as:
a1|a2|a3
b1|b2|b3
c1|c2|c3
"""

# Initialize the game board as a 2D list
board = [
    ["=", "=", "="],  # a1, a2, a3
    ["=", "=", "="],  # b1, b2, b3
    ["=", "=", "="]   # c1, c2, c3
]

player_symbol = "X"
computer_symbol = "O"
whos_turn_is_it = "X"

# Function to map position strings to board indices
def position_to_indices(position):
    # Map positions like "a1", "b2" to row and column indices
    row_map = {"a": 0, "b": 1, "c": 2}
    col_map = {"1": 0, "2": 1, "3": 2}
    
    if len(position) != 2 or position[0] not in row_map or position[1] not in col_map:
        return None
    
    return row_map[position[0]], col_map[position[1]]

def printboard():
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("-+-+-")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("-+-+-")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")

def gameisntover():
    # Check horizontal wins
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "=":
            return False
    
    # Check vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "=":
            return False
    
    # Check diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != "=":
        return False
    if board[0][2] == board[1][1] == board[2][0] != "=":
        return False
    
    # Check if the board is full (draw)
    is_full = True
    for row in range(3):
        for col in range(3):
            if board[row][col] == "=":
                is_full = False
                break
        if not is_full:
            break
    
    if is_full:
        return False
    
    return True

# Update player move to board
def update_player_position(position, player_symbol):
    indices = position_to_indices(position)
    
    if indices is None:
        print("Invalid position format. Use a1, b2, etc.")
        return False
    
    row, col = indices
    
    if board[row][col] == "=":
        board[row][col] = player_symbol
        return True
    else:
        print("Invalid Move - Position already taken")
        return False

def update_computer_position(computer_symbol):
    # Check for winning move
    for row in range(3):
        for col in range(3):
            if board[row][col] == "=":
                # Try the move
                board[row][col] = computer_symbol
                if not gameisntover():
                    # Winning move found
                    return True
                # Undo the move
                board[row][col] = "="
    
    # Check for blocking move
    for row in range(3):
        for col in range(3):
            if board[row][col] == "=":
                # Try the move for player
                board[row][col] = player_symbol
                if not gameisntover():
                    # Blocking move found
                    board[row][col] = computer_symbol
                    return True
                # Undo the move
                board[row][col] = "="
    
    # Take center if available
    if board[1][1] == "=":
        board[1][1] = computer_symbol
        return True
    
    # Take corners if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    import random
    random.shuffle(corners)
    
    for row, col in corners:
        if board[row][col] == "=":
            board[row][col] = computer_symbol
            return True
    
    # Take any available space
    for row in range(3):
        for col in range(3):
            if board[row][col] == "=":
                board[row][col] = computer_symbol
                return True
    
    return False

def get_winner():
    # Check horizontal
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "=":
            return board[row][0]
    
    # Check vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "=":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "=":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "=":
        return board[0][2]
    
    return None

# Main game loop
def play_game():
    global whos_turn_is_it
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, the computer is O")
    print("Enter positions as a1, b2, c3, etc.")
    
    while gameisntover():
        print(f"\nIt's {whos_turn_is_it}'s turn now!")
        printboard()
        
        if whos_turn_is_it == player_symbol:
            valid_move = False
            while not valid_move:
                user_move = input('Choose your move: ')
                valid_move = update_player_position(user_move, player_symbol)
            whos_turn_is_it = computer_symbol
        else:
            print("Computer is making a move...")
            update_computer_position(computer_symbol)
            whos_turn_is_it = player_symbol
    
    # Game over, show final board and result
    print("\nGame Over!")
    printboard()
    
    winner = get_winner()
    if winner:
        if winner == player_symbol:
            print("Congratulations! You won!")
        else:
            print("The computer won!")
    else:
        print("It's a draw!")

# Start the game if this file is run directly
if __name__ == "__main__":
    play_game()













