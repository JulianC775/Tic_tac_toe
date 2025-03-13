"""
board 
players
turns- location

to update board(will need a seperate function for computer)
check if position is valid(do for every position :(  ))
need global scope and to provide all possible legal moves
if
return false if not

I want some sort of decision for computer move not random

a1a2a3
b1b2b3
c1c2c3


computers (brain)
go in the middle
choose random corner
connect

"""
import random
a1,a2,a3,b1,b2,b3,c1,c2,c3 = "=","=","=","=","=","=","=","=","="
def printboard():
    print((a1),(a2),(a3))
    print((b1),(b2),(b3))
    print((c1),(c2),(c3))
player_symbol = "X"
computer_symbol = "O"
whos_turn_is_it = "X"



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
    if b2 == c2 and b2 == c2 and a2 != "=":
        return False
    if c3 == b3 and b3 == a3 and b3 != "=":
        return False
    #diagonal
    if a1 == b2 and b2 == c3 and a1 != "=":
        return False
    if a3 == b2 and b2 == c1 and a3 != "=":
        return False
    return True



#update player move to board
#todo: make it the computer's turn after you choose your move then your turn again
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
    

"""
2 = 1 
= X = 
3 = 4




"""




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
    #todo corners then endgamelogic(connect the corners)


while gameisntover():
    print(f" It's {whos_turn_is_it}'s turn now!")
    printboard()
    user_move = input('Choose your move')
    update_player_position(user_move,whos_turn_is_it)
    





printboard()













