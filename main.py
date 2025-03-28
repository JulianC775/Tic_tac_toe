"""
board 
players
turns- location

to update board(will need a seperate function for computer)
check if position is valid(do for every position :(  )
need global scope and to provide all possible legal moves
if
return false if not

if player has 2 in a row stop then stop the win

a1a2a3
b1b2b3
c1c2c3


computers (brain)
go in the middle
second should be checking if the player has 2 in a row then stop it
choose random corner
connect

"""
import random
#creates 9 variables and initilizes them to empty space on the board(=)
a1,a2,a3,b1,b2,b3,c1,c2,c3 = "=","=","=","=","=","=","=","=","="
def printboard():
    print((a1),(a2),(a3))
    print((b1),(b2),(b3))
    print((c1),(c2),(c3))
#assigns symbols to player and computer, initilizes it as players turn(in the future I want this to be random, it's the only way it's fair)
player_symbol = "X"
computer_symbol = "O"
whos_turn_is_it = "X"


#function that checks if either player has 3 in a row or a draw
def gameisntover():
    #horizonal
    if a1 == a2 and a2 == a3 and a1 != "=":
        return False
    if b1 == b2 and b2 == b3 and b1 != "=":
        return False
    if c1 == c2 and c2 == c3 and c1 != "=":
        return False
    #vertical
    if a1 == b1 and b1 == c1 and a1 != "=":
        return False
    if a2 == b2 and b2 == c2 and a2 != "=":
        return False
    if a3 == b3 and b3 == c3 and a3 != "=":
        return False
    #diagonal
    if a1 == b2 and b2 == c3 and a1 != "=":
        return False
    if a3 == b2 and b2 == c1 and a3 != "=":
        return False
    
    if "=" not in [a1, a2, a3, b1, b2, b3, c1, c2, c3]:
        print("Board is full - it's a draw!")
        return False
    
    return True



#update player move to board based off of user input

def update_player_position(position, player_symbol):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    if position == "a1" and a1 == "=":
        a1 = player_symbol
        return True
    elif position == "a2" and a2 == "=":
        a2 = player_symbol
        return True
    elif position == "a3" and a3 == "=":
        a3 = player_symbol
        return True
    elif position == "b1" and b1 == "=":
        b1 = player_symbol
        return True
    elif position == "b2" and b2 == "=":
        b2 = player_symbol
        return True
    elif position == "b3" and b3 == "=":
        b3 = player_symbol
        return True
    elif position == "c1" and c1 == "=":
        c1 = player_symbol
        return True
    elif position == "c2" and c2 == "=":
        c2 = player_symbol
        return True
    elif position == "c3" and c3 == "=":
        c3 = player_symbol
        return True
    else:
        print("Invalid Move")
        return False
    


#computer brain logic

def update_computer_position(computer_symbol):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    #step 1, choose the middle if available
    if b2 == "=":
        b2 = computer_symbol
        return True
    #step 2, list all possible legal moves
    available_positions = []
    if a1 == "=": available_positions.append("a1")
    if a2 == "=": available_positions.append("a2")
    if a3 == "=": available_positions.append("a3")
    if b1 == "=": available_positions.append("b1")
    if b3 == "=": available_positions.append("b3")
    if c1 == "=": available_positions.append("c1")
    if c2 == "=": available_positions.append("c2")
    if c3 == "=": available_positions.append("c3")
    if not available_positions:
        return False
        
    #step 3, choose a corner then correspoonding corner
    corners = ["a1","a3","c1","c3"]
    available_corners = [pos for pos in corners if pos in available_positions]

    #must first check if corresponding corner is available
    if available_corners:
        if "a1" in available_corners and a3 == computer_symbol:
            chosen_position = "a1"  # Take a1 if we already have a3
        elif "a3" in available_corners and a1 == computer_symbol:
            chosen_position = "a3"  # Take a3 if we already have a1
        elif "c1" in available_corners and c3 == computer_symbol:
            chosen_position = "c1"  # Take c1 if we already have c3
        elif "c3" in available_corners and c1 == computer_symbol:
            chosen_position = "c3"  # Take c3 if we already have c1
        else:
        # If no corresponding corner pattern found, take any random available corner
            chosen_position = random.choice(available_corners)
        
        #update the board with the chosen corner
        if chosen_position == "a1": a1 = computer_symbol
        elif chosen_position == "a3": a3 = computer_symbol
        elif chosen_position == "c1": c1 = computer_symbol
        elif chosen_position == "c3": c3 = computer_symbol
        return True
    




while gameisntover():
    #prints a line between moves
    print("\n" + "-"*20)
    print(f"It's {whos_turn_is_it}'s turn now!")
    printboard()
    user_move = input('Choose your move')
    

    valid_move = update_player_position(user_move,whos_turn_is_it)
    if valid_move:
        #check if game is over after the player moves
        if not gameisntover():
            break

        #now it's the computers turn
        print("\nComputers Turn:")
        update_computer_position(computer_symbol)

        # Check if game is over after computer's move
        if not gameisntover():
            break
#prints the board after a valid move, need a case for it to print on invalid move since that would be more important
    print("\nTile Locations")
    print("a1,a2,a3")
    print("b1,b2,b3")
    print("c1,c2,c3")



#print final board state
print("Game Over!")
printboard()

# Show who won
if a1 == a2 == a3 != "=": 
    print(f"Winner: {a1}")
elif b1 == b2 == b3 != "=": 
    print(f"Winner: {b1}")
elif c1 == c2 == c3 != "=": 
    print(f"Winner: {c1}")
elif a1 == b1 == c1 != "=": 
    print(f"Winner: {a1}")
elif a2 == b2 == c2 != "=": 
    print(f"Winner: {a2}")
elif a3 == b3 == c3 != "=": 
    print(f"Winner: {a3}")
elif a1 == b2 == c3 != "=": 
    print(f"Winner: {a1}")
elif a3 == b2 == c1 != "=": 
    print(f"Winner: {a3}")
else:
    print("It's a draw!")













