import random
n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
if 1 < guess > 100:
    print("not in range")

else:


while n != "guess":
    print ("not good")
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break
    print ("won the game")