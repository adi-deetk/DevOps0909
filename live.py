from GuessGame import GG

def welcome():
    name = str(input("Enter your name:" ))
    print("Hello " + name + " and welcome to the World of Games (WoG). \nHere you can find many cool games to play.\n",("-"*50))


def load_game():
    print("\nPlease choose a game to play:", end =" ")
    a = "\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back"
    b = "\n2. Guess Game - guess a number and see if you chose like the computer"
    c = "\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS"
    print(a,b,c,("\n" + "-"*80))

    print("Enter the game number 1-3 :")
    game_op = int(input())
    if game_op == int(1):
        print("You have selected: " + str(a) + GG())
    elif game_op == int(2):
        print("You have selected: " + str(b))
    elif game_op == int(3):
        print("You have selected: " + str(c))
    else:
        print("Error: only select 1 until 3")
        return game_op





