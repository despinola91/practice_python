# Exercise:
# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 
# Download this file and save it in the same directory as your Python code. 
# This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. 
# Each line in the file contains a single word.

# Hint: use the Python random library for picking a random word.

# Aside: what is SOWPODS
# SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example).
#  It is the combination of the Scrabble Player’s Dictionary and the Chamber’s Dictionary.
#  (The history of SOWPODS is quite interesting, I highly recommend reading the Wikipedia article if you are curious.)
import random

words = list()
limit = 0

def print_random_word(index):
    print("Printing random word: " + words[int(index)])


def read_words():
    global limit
    
    with open("scrabble_words.txt", "r") as file:
        line = file.readline()
        limit = limit + 1
    
        while line:
            words.append(line)
            line = file.readline()
            limit = limit + 1

def run():
    read_words()

    index = random.randint(1, int(limit))
    print_random_word(index)

if __name__ == "__main__":
    run()