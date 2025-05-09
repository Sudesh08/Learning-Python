# 8. Number Guessing Game
# Create a function that generates a random number and lets the user guess it in a loop until correct,
# giving hints (higher/lower).
import random

def isEqualToRandomNumber():
    randomNumber = random.randint(1, 100)
    # print(randomNumber)
    userNumber = int(input("Enter number between 1-100 "))
    while randomNumber != userNumber:
        if randomNumber > userNumber:
            print("Wrong guess! Number is Lower")
            userNumber=int(input("PLease enter number again "))
        elif randomNumber<userNumber:
            print("Wrong Guess! Number is Greater")
            userNumber = int(input("PLease enter number again "))
    print("Hurry You Win the game !")
isEqualToRandomNumber()


