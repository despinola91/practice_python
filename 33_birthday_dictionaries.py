# Exercise:
# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

# This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. 
# Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 
# The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

birthdays = {
	"Albert Einstein": "05/14/1879",
	"Charles Chaplin": "04/16/1889",
    "San Martin": "02/25/1778",
	"Nestor Kirchner": "02/25/1950"
}

def show_birthday(name):
    date = birthdays.get(name, "unknown as we don't have this name in the list!")
    print(">>> {}'s birthday is {}.".format(name, date))

def run():
    print(">>> Welcome to the birthday dictionary. We know the birthdays of:\n")
    for key in birthdays.keys():
        print(key)

    name = input("\n>>> Who's birthday do you want to look up?\n")
    show_birthday(name)

if __name__ == "__main__":
    run()