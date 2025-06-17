import random

def game():
    newScore = random.randint(1, 50)
    with open("score.txt","r") as file:
        highScore=file.read()
        if highScore=="" :
            highScore=0
            print(highScore)

    print(newScore,"Print 3")
    if newScore>int(highScore):
        with open("score.txt","w") as filewrite:
            filewrite.write(str(newScore))

game()