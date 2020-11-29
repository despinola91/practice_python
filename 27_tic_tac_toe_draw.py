# Exercise:
# https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

# This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.
# In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game. 
# In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).

# There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.
# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. 
# So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.

# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:
# game = [[0, 0, 0],
#   	[0, 0, 0],
#   	[0, 0, 0]]
# The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out

# game = [[0, 0, X],
# 	    [0, 0, 0],
# 	    [0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.

# Things to note:

# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). 
# To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. 
# This is not required, but whichever way you choose to implement this, it should be explained to the player.

# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. 
# Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, 
# do not allow the piece to go there.

# Bonus:
# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full. 
# In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.


def mark_square(row, col, value):
    global game
    if value == 1: value = "X"
    if value == 2: value = "O"

    game[int(row)-1][int(col)-1] = value

def clear_zeros(value):
    if value != 0:
        return str(value)
    else:
        return " "

def draw(game):

    count = 0
    for el in range(int(3)):
        print(" ---" + " ---" + " --- ")
        
        print("| " + clear_zeros(game[count][0]) + " " + "| " + clear_zeros(game[count][1]) + " "+ "| " + clear_zeros(game[count][2]) + " |")
        count = count + 1
            
    print(" ---" + " ---" + " --- ")
    
def are_valid_coordinates(row, col):
    return game[int(row)-1][int(col)-1] == 0

def init():
    print(" ---- Welcome to tic tac toe! ---- \n\n")
    draw(game)
    print("\n\n")

def get_msg(player):
    msg = ""

    if player == 1:
        msg = "Hello player 1, please enter the coordinates of the square you want to use in the form 'row,column', for example 1,2:\n"
    elif player == 2:
        msg = "Hello player 2, please enter the coordinates of the square you want to use in the form 'row,column', for example 1,2:\n"
    
    return msg

def change_player():
    global player
    if player == 1:
        player = 2
    elif player == 2:
        player = 1

def check_spaces():
    global there_are_available_spaces
    there_are_available_spaces = False

    for row in game:
        for col in row:
            if col == 0:
                there_are_available_spaces = True
                break

def finalize():
    print("\nThe game has ended!")


game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

player = 1
there_are_available_spaces = True

def run():
    #showing init page
    init()


    while there_are_available_spaces == True:
        #asking for coordinates to the corresponding user
        coordenates = input(get_msg(player))

        #getting valid coordiantes
        row = coordenates.split(",")[0]
        col = coordenates.split(",")[1]

        if are_valid_coordinates(row, col) == True:
            change_player()
            mark_square(row, col, player)
            draw(game)
            check_spaces()
        else:
            print("That place is already taken!\n")
    
    finalize()

if __name__ == "__main__":
    run()