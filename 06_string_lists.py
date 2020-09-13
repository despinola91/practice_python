# Exercise:
# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

def run():
    text = input("Please insert your text: ")
    if text == text[::-1]:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome!")
        

if __name__ == "__main__":
    run()