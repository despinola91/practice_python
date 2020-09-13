# Exercise:
# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

def run():
    
    #Asking for number and validating data type
    valid_number = False
    while valid_number == False:
        try:
            number = int(input("Please insert your number: "))
            valid_number = True
        except:
            print("Please insert a number.\n")

    #Extra 1
    if number % 4 == 0:
        print("Your number multiple of 4!")
    else:
        if number % 2 == 0:
            print("Your number is even")
        else:
            print("Your number is odd")

    #Extra 2
    valid_num = False
    while valid_num == False:
        try:
            num = int(input("Please insert a number to check: "))
            valid_num = True
        except:
            print("Please insert a number.\n")

    valid_check = False
    while valid_check == False:
        try:
            check = int(input("Please insert a number to divide by: "))
            valid_check = True
        except:
            print("Please insert a number.\n")

    if num % check == 0:
        print(str(num) + " divides evenly into " + str(check))
    else:
        print(str(num) + " does not divide evenly into " + str(check))

if __name__ == "__main__":
    run()