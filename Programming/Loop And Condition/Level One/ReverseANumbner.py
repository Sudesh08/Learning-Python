# 15. Reverse a Number
# Write a function to reverse the digits of a number using a loop.

def reverseNumber(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n//=10
    return rev

num=int(input("Enter number to reverse : "))
print(reverseNumber(num))