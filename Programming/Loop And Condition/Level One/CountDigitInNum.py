# 13. Count Digits in a Number
# Write a function that takes an integer and counts the number of digits using a loop.

def countDigitInNumber(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c

Num=int(input("Enter a number : "))
print(countDigitInNumber(Num))