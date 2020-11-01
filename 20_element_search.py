# Exercise:
# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:
# Use binary search.

import math

def binay_search(arr, x):
    # Declaramos los índices de las posiciones minima, media y máxima.
    low = 0
    mid = 0
    high = len(arr) - 1
  
    while low <= high: # Mientras el índice del mínimo sea menor o igual al índice del máximo...
  
        mid = (high + low) // 2
  
        # Revisamos si el valor en el índice medio es menor al valor buscado. Si es así, seteamos un nuevo índice mínimo
        if arr[mid] < x: 
            low = mid + 1
  
        # Revisamos si el valor en el índice medio es mayor al valor buscado. Si es así, seteamos un nuevo índice máximo
        elif arr[mid] > x: 
            high = mid - 1
  
        # Si el valor en el índice medio no es menor mi mayor significa que es el valor buscado
        else: 
            return True
  
    # Si llegamos a este punto significa que el valor buscado no existe en la lista
    return False


def run():
    numbers = [1, 3, 5, 7, 9, 13, 15, 21, 98, 120, 156, 163, 785, 950, 1523]
    number = int(input("Pick the number!\n"))
    result = binay_search(numbers, number)

    print("It is", str(result), "that the number", number, "exits in the list.")


if __name__ == "__main__":
    run()