# Exercise:
# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
import sys

def get_number():
    while True:
        number = input("Please enter the amount of Fibonacci numbers to generate:\n")
        
        if number == "exit": sys.exit()

        try:
            number = int(number)
            break
        except:
            print("That was not a number.\n")

    return number


def generate_sequence(number):
    sequence = list()

    for i in range(number):
        if i == 0:
            sequence.append(1)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i-2]+sequence[i-1])
    
    return sequence


def run():
    while True:
        number = get_number()
        sequence = generate_sequence(number)
        print(sequence)

if __name__ == "__main__":
    run()