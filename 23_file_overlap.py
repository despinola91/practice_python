# Exercise:
# # https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. 
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

def load_prime_numbers():
    with open("primenumbers.txt", "r") as primes_file:
        n = primes_file.readline()
        while n:
            n = n.strip()
            prime_numbers.append(n)
            n = primes_file.readline()

    print("\n\n--- Prime numbers---")
    print(prime_numbers)


def load_happy_numbers():
    with open("happynumbers.txt", "r") as happy_file:
        n = happy_file.readline()
        while n:
            n = n.strip()
            happy_numbers.append(n)
            n = happy_file.readline()

    print("\n\n--- Happy numbers---")
    print(happy_numbers)

def find_overlapped_numbers():
    for num in prime_numbers:
        if num in happy_numbers:
            overlapped_numbers.append(num)

    print("\n\n--- Overlapped numbers---")
    print(overlapped_numbers)

def run():
    global prime_numbers
    prime_numbers = list()

    global happy_numbers
    happy_numbers = list()

    global overlapped_numbers
    overlapped_numbers = list()

    load_prime_numbers()
    load_happy_numbers()
    find_overlapped_numbers()


if __name__ == "__main__":
    run()