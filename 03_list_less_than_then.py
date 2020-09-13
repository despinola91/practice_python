# Exercise:
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html


def run():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new_list = list()

    for element in a:
        if element > 5:
            #Extra 1
            new_list.append(element)

    print(new_list)

    #Extra 3
    new_list_smaller = list()
    valid_number = False
    while valid_number == False:
        try:
            number = int(input("Please insert a number: "))
            valid_number = True
        except:
            print("Please insert a number.\n")

    for i in a:
        if i<number:
            new_list_smaller.append(i)
    
    print(new_list_smaller)

if __name__ == "__main__":
    run()