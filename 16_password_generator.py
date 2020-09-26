# Exercise:
# https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import random

def generate_password(length):
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbolos = ["!", "#", "$", "&", "/", "(", ")"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range (length):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)
    return password


def run():
    while True:
        length = input("How many characters do you want in your password?: ")
        if length == "exit":
            break
        
        password = generate_password(int(length))
        print("New password: " + password)


if __name__ == "__main__":
    run()