# Exercise:
# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

def run():
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    #Extra 1 --> Generating 2 random lists
    a = list()
    b = list()

    for i in range(random.randint(40,50)):
        a.append(random.randint(1,50))

    for i in range(random.randint(40,50)):
        b.append(random.randint(1,50))


    new_list = list()
    print (a)
    print (b)

    # Per each element in a we add it to new list only if --> element exists also in b and does not exist in new_list (duplicate)
    new_list = [elem for elem in a if elem in b and elem not in new_list]

    # for elem in a:
    #     if elem in b and elem not in new_list: new_list.append(elem)

    print(new_list)

if __name__ == "__main__":
    run()