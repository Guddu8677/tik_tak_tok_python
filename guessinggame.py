#number gussing game
import random
generate=random.randint(1 ,10)
guess =int(input("Guess a number"))

while True:
    if(guess == generate):
        print("correct guess")
        break
    if guess <generate:
        print("guess higher")
    else:
        print("guess lower")
    guess =int(input("enter again number"))
      


