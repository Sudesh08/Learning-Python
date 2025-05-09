# 14. Armstrong Number Checker
# Create a function that checks if a number is an Armstrong number (e.g., 153 = 1³ + 5³ + 3³).

def countOfNum(n):
    c=0
    while n>0:
        c = c + 1
        n//=10
    return c

def findSqrt(digit,numberOfRotation):
    return digit**numberOfRotation

def isArmstrongNumber(n):
    temp=n
    add=0
    while temp>0:
        r=temp%10
        add=add+findSqrt(r,countOfNum(n))
        temp=temp//10
    return add==n

Num=int(input("Enter positive number to check Armstrong Number : "))
if Num<0:
    print("Number is not valid")
else:
    print("Armstrong Number" if isArmstrongNumber(Num) else "Not Armstrong Number")