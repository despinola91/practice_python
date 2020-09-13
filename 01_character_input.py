# Exercise:
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import date
current_year = date.today().year

def run():

    #Asking for name
    name = input("Please enter your name: ")
    
    #Asking for age and validating data type
    age_is_ok = False
    while age_is_ok == False:
        try:
            age = int(input("Please enter your age: "))
            age_is_ok = True
        except:
            print("Please insert a number.\n")
    
    #Asking for repetition number and validating data type
    repeat_is_valid = False
    while repeat_is_valid == False:
        try:
            repeat = int(input("How many times do you want to see the message?: "))
            repeat_is_valid = True
        except:
            print("Please insert a number.\n")

    for i in range(repeat):
        print(name + " you will turn 100 years old in year " + str(int(current_year) + (100 - age)))

if __name__ == "__main__":
    run()