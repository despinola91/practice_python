# Exercise:
# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html


def get_max(numbers):
    max = 0
    for number in numbers:
        if int(number) > max: max = int(number)
    return str(max)


def run():
    variables = input("Please enter the 3 variables separated by comma:\n")
    numbers = variables.split(",")
    
    print("The maximum value is " + get_max(numbers))


if __name__ == "__main__":
    run()