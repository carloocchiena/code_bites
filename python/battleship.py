#import the random function
from random import randint

#create the game board (5x5)
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

#let's begin to play. 4 turn to guess where is the ship
print "Let's play Battleship!"
print "You have 4 match to play"

#printing the game board
print_board(board)

#define where the boat is located, using the random function, with len to locate within the game board 
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#commented line used to show position of battle code

#print ship_row
#print ship_col

#the first turn start
for turn in range(4):
    print "Turn", turn+1
    print "%s turn left" % (4-turn)
    #guess_row = int(raw_input("Guess Row:"))
    #guess_col = int(raw_input("Guess Col:"))
    #using try to catch null value
    try:
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
    except ValueError:
        print "You must input a value"
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        print "Game Over"
        break 
    
    else:
        if (guess_row < 0 or guess_row > 4) \
        or (guess_col < 0 or guess_col > 4) :
            print "Oops, that's not even in the ocean."
        
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)

if turn==3:
    print "Game Over"
