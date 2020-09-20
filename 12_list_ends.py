# Exercise:
# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

def get_new_list(a):
    return [a[0], a[len(a) - 1]]

def run():
    a = [5, 10, 15, 20, 25]    
    new_list = get_new_list(a)
    print(new_list)

if __name__ == "__main__":
    run()