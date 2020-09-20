# Exercise:
# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random
import sys

def run():
    
    while True:
        
        print("\n\n *** Welcome to the guessing game!  *** \n\n")
        
        random_num = random.randint(1,9)
        # Debug
        # print("randon number:", random_num)
        guesses = 0
            
        valid_number = False
        match_ended = False
        number = None
        message = "Guess the number between 1 and 9!\n"

        while match_ended == False:
            
            number = input(message)
            
            if number == "exit":
                sys.exit()
            else:
                try:
                    number = int(number)
                    guesses += 1
                    valid_number = True
                except:
                    print("That was not a number!\n\n")

            if valid_number == True:
                if random_num == number:
                    print("You won!")
                    print("Amount of guesses:", guesses)
                    match_ended = True
                elif random_num > number:
                    message = "Too low! Guess again\n"
                elif random_num < number:
                    message = "Too high! Guess again\n"

if __name__ == "__main__":
    run()