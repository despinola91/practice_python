# Exercise:
# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

# This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.
# You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).
# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose 
# the game.

# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
# In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
#     Only let the user guess 6 times, and tell the user how many guesses they have left.
#     Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

# Optional additions:
#     When the player wins or loses, let them start a new game.
#     Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. 
#     This is challenging - do the other parts of the exercise first!

import random

def show_result():
    final_result = ""
    for letter in result:
        final_result = final_result + letter + " "
    print(final_result + "\n")

def analyze_letter(letter):
    global result
    global guesses
    
    found = False
    for i in range(len(word)):
        if letter == word[i]:
            found = True
            result[i] = word[i]
    
    if found == False:
        guesses = guesses + 1
        print("Incorrect!")
        print("Guesses left: " + str(6 - guesses))

def get_random_word():
    words = list()
    counter = 0
    
    with open('scrabble_words.txt', "r") as file_object:
        for line in file_object:
            counter = counter + 1
            words.append(line.strip())
    
    chosen_word = words[random.randint(1, counter)]

    print("the word is: " + chosen_word) #just a helper to be removed
    return chosen_word.upper()

word = ""
result = list()
guesses = 0

def init():
    print("\n>>> Welcome to Hangman!")
    
    global word
    word = get_random_word()

    #Setting result variable at the beginning
    for l in word: 
        result.append("_")

def run():

    init()

    while True:
        show_result()

        letter = input(">>> Guess your letter:")
        letter = letter.upper()

        if letter == "EXIT" or letter == "QUIT":
            exit()
        
        if letter == word:
            print("You guessed the word!")
            break

        analyze_letter(letter)
        
        game_on = False
        for l in result:
            if l == "_":
                game_on = True
        
        if game_on == False:
            print("You guessed the word!")
            break

if __name__ == "__main__":
    run()