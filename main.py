"""
board 
players
turns- location

win = 3 in row
else tie

a1a2a3
b1b2b3
c1c2c3

"""
a1,a2,a3,b1,b2,b3,c1,c2,c3 = "=","=","=","=","=","=","=","=","="
def printboard():
    print((a1),(a2),(a3))
    print((b1),(b2),(b3))
    print((c1),(c2),(c3))
player1 = "X"
player2 = "O"
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
    if b2 == c2 and c2 == a2 and b2 != "=":
        return False
    if c3 == b3 and b3 == a3 and b3 != "=":
        return False
    #diagonal
    if a1 == b2 and b2 == c3 and a1 != "=":
        return False
    if a3 == b2 and b2 == c1 and a3 != "=":
        return False
    return True



while gameisntover():
    print(whos_turn_is_it)
    print('a1a2a3')
    print('b1b2b3')
    print('c1c2c3')
    user_move = input('Choose your move')




printboard()













