# Create a game for stone paper and Sizer
from logging import exception
from random import random


computerValue=2
value={
    "Stone":1,
    "Paper":2,
    "Sizer":3
}

userInput=input("Enter your choice : Stone or Paper or Sizer ")
newValue =-1
try:
    newValue=value[userInput]
    if newValue == 1 or newValue == 2 or newValue != 3:
        if newValue == computerValue:
            print("Match Draw")
        else:
            if newValue == 2 and computerValue == 1:
                print("You win!")
            elif newValue == 3 and computerValue == 1:
                print("You lose!")
            elif newValue == 1 and computerValue == 2:
                print("You Lose!")
            elif newValue == 3 and computerValue == 2:
                print("You win!")
            elif newValue == 1 and computerValue == 3:
                print("You Win!")
            elif newValue == 2 and computerValue == 3:
                print("You Lose!")
except KeyError:
    print("Invalid input")

