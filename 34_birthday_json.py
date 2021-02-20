# Exercise:
# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# 
# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.
# In the previous exercise we created a dictionary of famous scientists’ birthdays. 
# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, 
# rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, 
# and update the JSON file you have on disk with the scientist’s name.
# If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.

import json

def get_birthdays():
    with open("34_birthdays.json", "r") as f:
        birthdays = json.load(f)

    return birthdays
    
def save_birthdays(birthdays):
    with open("34_birthdays.json", "w") as f:
        json.dump(birthdays, f)

def show_birthday(birthdays, name):
    date = birthdays.get(name, "unknown as we don't have this name in the list!")
    print(">>> {}'s birthday is {}.".format(name, date))

def run():
    print(">>> Welcome to the birthday dictionary. We know the birthdays of:\n")

    birthdays = get_birthdays()
    for key in birthdays.keys():
        print(key)

    name = input("\n>>> Who's birthday do you want to look up?\n")
    show_birthday(birthdays, name)

if __name__ == "__main__":
    run()
