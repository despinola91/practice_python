# Exercise:
# https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html

# This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.

# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player 
# has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. 
# (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player 
# to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess 
# an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed 
# and display a different message if the player tries to guess that letter again. Remember to stop the game when all 
# the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number 
# of guesses the player has remaining - we will deal with those in a future exercise.

# An example interaction can look like this:

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.

import random

def show_result():
    a = ""
    for l in result:
        a = a +l+" "
    print(a+"\n")

def analyze_letter(letter):
    global result

    for i in range(len(word)):
        if letter == word[i]:
            result[i] = word[i]


def get_random_word():
    return "evaporate"

word = ""
result = list()

def run():
    print("\n>>> Welcome to Hangman!")
    global word
    word = get_random_word()

    for l in word:
        result.append("_")

    while True:
        show_result()
        letter = input(">>> Guess your letter:")
        
        if letter == "exit":
            exit()

        analyze_letter(letter)

if __name__ == "__main__":
    run()