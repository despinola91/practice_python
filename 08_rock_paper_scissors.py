# Exercise:
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

def run():
    options = """\n*** Options ***
    a - Rock
    b - Paper
    c - Scissors\n"""
    
    while True:
        print(options)
        player_a = input("Player A insert option: ")
        player_b = input("Player B insert option: ")

        if player_a == "a":
            if player_b == "a":
                print("It is a tie!")
            if player_b == "b":
                print("Player B won!")
            if player_b == "c":
                print("Player A won!")

        if player_a == "b":
            if player_b == "a":
                print("Player A won!")
            if player_b == "b":
                print("It is a tie!")
            if player_b == "c":
                print("Player B won!")

        if player_a == "c":
            if player_b == "a":
                print("Player B won!")
            if player_b == "b":
                print("Player A won!")
            if player_b == "c":
                print("It is a tie!")

        play_again = input("\nDo you want to play again? (yes/no) ")
        if play_again == "no":
            break

if __name__ == "__main__":
    run()