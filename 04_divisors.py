# Exercise:
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

def run():
    number = int(input("Please insert a number: "))
    x = list(range(1, number + 1))

    for elem in x:
        if number % elem == 0:
            print(elem)

if __name__ == "__main__":
    run()