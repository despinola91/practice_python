# Exercise:
# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

def run():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    #Long way
    # new_list = list()
    # for elem in a:
    #     if elem % 2 == 0:
    #         new_list.append(elem)

    #One line way
    new_list = [elem for elem in a if elem % 2 == 0]

    print(new_list)

if __name__ == "__main__":
    run()