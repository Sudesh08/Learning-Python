# 5. Prime Number Checker
# Write a function that checks whether a number is prime or not using a loop and condition.
from itertools import count

def checkNumberIsPrimeOrNot(num):
    if num <= 1:
        return False  # 0 and 1 are not prime

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Not a prime number
    return True  # Prime number

number = int(input("Enter number to check whether it is prime or not: "))
result = "Prime number" if checkNumberIsPrimeOrNot(number) else "Not a prime number"
print(result)

# number=int(input("Enter number to check weather a number is prime or not : "))
# def checkNumberIsPrimeOrNot(num):
#     c=0
#     for i in range(1,num/2+1):
#         if num % i==0:
#            c+=1
#
#         return c
#
# result = "Prime number" if checkNumberIsPrimeOrNot(number)>2 else "Not a prime number"
# print(result)