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
fileName = "34_birthdays.json"
birthdays = dict()


def load_birthdays():
    global birthdays
    with open(fileName, "r") as f:
        birthdays = json.load(f)


def save_birthdays(birthdays):
    with open(fileName, "w") as f:
        json.dump(birthdays, f)


def show_birthday(name):
    date = birthdays.get(name, "unknown as we don't have this name in the list")
    print(">>> {}'s birthday is {}.".format(name, date))


def add_birthday(name, birthday):
    birthdays[name] = birthday
    save_birthdays(birthdays)
    print(">>> The new record was added.")


def show_complete_list():
    print(">>> We know the birthdays of:\n")
    load_birthdays()
    for key in birthdays.keys():
        print(key)


def get_birthday():
    name = input("\n>>> Who's birthday do you want to look up?\n")
    show_birthday(name)


def create_birthday():
    newName = input(">>> Please enter the name of the person:\n")
    newBirthday = input(">>> Please enter the person's birthday with format mm/dd/yyyy:\n")
    add_birthday(newName, newBirthday)


def run():
    print("\n>>> Welcome to the birthday dictionary.")

    while True:
        option = input(
        """\n>>> What would you like to do?
        1. See complete list of available birthdays
        2. Look up someone's birthday
        3. Add a new birthday\n\n""")
        
        if option == "1":
            show_complete_list()
        elif option == "2":
            get_birthday()
        elif option == "3":
            create_birthday()
        elif option.lower() == "leave" or option.lower() == "exit" or option.lower() == "quit":
            exit()
        else:
            print(">>> The entered value is not valid.")

if __name__ == "__main__":
    run()
