# Exercise:
# https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

# This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.

# In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:

# Draw the Tic Tac Toe game board
# Checking whether a game board has a winner
# Handle a player move from user input

# The next step is to put all these three components together to make a two-player Tic Tac Toe game! 
# Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a 
# two-player game that you can play with a friend. 
# There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.

# Here are a few things to keep in mind:

# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.
import re

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

player = 1
there_are_available_spaces = True
winner = ""
game_over = False
scores = {
    "player_1": 0,
    "player_2": 0
}

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
    print("\n")
    
def is_place_available(row, col):
    row_index = int(row)-1
    col_index = int(col)-1
    return game[row_index][col_index] == 0

def init():
    print("\n\n")
    print("---------------------------------")
    print("|                               |")
    print("|    Welcome to tic tac toe!    |")
    print("|                               |")
    print("---------------------------------")
    #draw(game)
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

def restart_board():
    global game
    global there_are_available_spaces
    global winner
    global player

    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    there_are_available_spaces = True
    winner = ""
    player = 1
    print("\n")
    draw(game)

def finalize():
    global game_over

    print("\nThe game has ended!\n")
    if winner != "":
        print("--------------------------------")
        print("|                              |")
        print("|  " + winner + " has won the game!  |")
        print("|                              |")
        print("--------------------------------")

        print(" ---------- Score --------- ")
        print("|  Player 1       Player 2 |")
        print("|                          |")
        print("|    ***            ***    |")
        print("|   * "+str(scores["player_1"])+" *          * "+str(scores["player_2"])+" *   |")
        print("|    ***            ***    |")
        print(" -------------------------- ")

        play_again = input("Do you want to play again? (yes/no)\n")
        if play_again == "no":
            game_over = True
            print("\nGoodbye!")
        elif play_again == "yes":
            restart_board()

def check_winner():
    global winner
    global there_are_available_spaces
    global scores

    #Checking horizontal possibilities
    if game[0][0] == game[0][1] == game[0][2] != 0:
        if game[0][0] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"
    if game[1][0] == game[1][1] == game[1][2] != 0:
        if game[1][0] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"
    if game[2][0] == game[2][1] == game[2][2] != 0:
        if game[2][0] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"

    #Checking vertical possibilities
    if game[0][0] == game[1][0] == game[2][0] != 0:
        if game[0][0] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"
    if game[0][1] == game[1][1] == game[2][1] != 0:
        if game[0][1] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"
    if game[0][2] == game[1][2] == game[2][2] != 0:
        if game[0][2] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"

    #Checking diagonal possibilities
    if game[0][0] == game[1][1] == game[2][2] != 0:
        if game[0][0] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"
    if game[0][2] == game[1][1] == game[2][0] != 0:
        if game[0][2] == "X":
            winner = "Player 1"
        else:
            winner = "Player 2"

    if winner != "":
        there_are_available_spaces = False
        if winner == "Player 1":
            scores["player_1"] = scores["player_1"] + 1
        elif winner == "Player 2":
            scores["player_2"] = scores["player_2"] + 1
        return True
    
    return False

def check_coordenates(coordenates):
    are_valid = False

    no_spaces_coordenates = re.sub(" ", "", coordenates)
    if len(no_spaces_coordenates) == 3:
        if no_spaces_coordenates[1] == ",":
            try:
                row = int(no_spaces_coordenates[0])
            except:
                return False

            try:
                col = int(no_spaces_coordenates[2])
            except:
                return False
            

            if (row > 0 and row < 4) and (col > 0 and col < 4):
                are_valid = True
    
    return are_valid
        
        
def run():
    #showing init page
    init()
    draw(game)
    while game_over == False:
        while there_are_available_spaces == True:
            #asking for coordinates to the corresponding user
            coordenates = input(get_msg(player))

            if coordenates == "exit" or coordenates == "quit" or coordenates == "leave" or coordenates == "stop":
                exit()

            if check_coordenates(coordenates) == False:
                print("Those are not valid coordinates. Please try again!\n")
                continue

            #getting valid coordiantes
            clean_coordenates = re.sub(" ", "", coordenates)
            row = clean_coordenates.split(",")[0]
            col = clean_coordenates.split(",")[1]

            #if are_valid_coordinates(row, col) == True:

            if is_place_available(row, col) == True:
                mark_square(row, col, player)
                draw(game)
                check_winner()

                if there_are_available_spaces == True:
                    change_player()
                    check_spaces()
            else:
                print("That place is already taken. Please try again!\n")

            # else:
            #     print("Those are not valid coordinates. Please try again!\n")
        finalize()

if __name__ == "__main__":
    run()