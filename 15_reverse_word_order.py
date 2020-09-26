# Exercise:
# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html


def get_reversed_phrase(phrase):
    words = phrase.split()
    words.reverse()
    new_phrase = " ".join(words)
    return new_phrase


def run():
    phrase = input("Please insert your phrase:\n")
    reversed_phrase = get_reversed_phrase(phrase)
    print(reversed_phrase)

if __name__ == "__main__":
    run()