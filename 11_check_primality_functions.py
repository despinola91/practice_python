# Exercise:
# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
import sys

def get_number():
    while True:
        number = input("\nEnter a number: ")
        
        if number == "exit" or number == "done":
            sys.exit()

        try:
            number = int(number)
            break
        except:
            print("That was not a number, try again.\n")

    return number

def analyse_number(numero):
    
    # Para saber si un número es primo (divisible sólo por el mismo y por uno), lo dividimos sucesivamente por los primeros números primos: 2, 3, 5, 7, 11, ..
    # ¿Cuándo paramos de dividir?

    # - Si obtenemos división exacta --> no es primo
    # - Si el cociente es menor que el divisor .. paramos --> es primo

    # Ejemplo: 113

    # - 113 no es divisible por 2 (divisor: 2 , cociente: 56.5)
    # - 113 no es divisible por 3 (divisor: 3 , cociente: 37’ ..)
    # - 113 no es divisible por 5 (divisor: 5 , cociente: 22’ ..)
    # - 113 no es divisible por 7 (divisor: 7 , cociente: 16’ ..)
    # - 113 no es divisible por 11 (divisor: 11 , cociente: 10’ ..)
    # Paramos pues el cociente es menor que el divisor --> 113 es primo

    primeros_primos = [2,3,5,7,11]
    for primo in primeros_primos:
        cociente = numero / primo
        resto = numero % primo
        # Debug
        # print("Primo: " + str(primo))
        # print("Cociente: " + str(cociente))
        # print("Resto: " + str(resto))
        if resto == 0:
            return False
        elif cociente < primo:
            return True

def run():
    while True:
        number = get_number()
        is_prime = analyse_number(number)

        if is_prime is True:
            print("Your number is prime.")
        else:
            print("Your number is not prime.")


if __name__ == "__main__":
    run()