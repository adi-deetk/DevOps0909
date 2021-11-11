import random
def GG():
    u_difficulty = int(input("play a guess game.\nselect the level of difficulty from 1 to 100:"))
    if 1 > u_difficulty > 100:
        print("wrong number")

    u_guess = int(input("Pick a number between 1 to " + str(u_difficulty) + ":"))
    if 1 > u_guess > 100:
        print("wrong number")

    game = random.randint(1, u_difficulty)

    while u_guess == game:
        print("you won!!")
    if u_guess > game:
        print("too high")
    else:
        print("too low")

    print(GG())