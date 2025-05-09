#
# 4. Factorial Calculator
# Create a function that calculates the factorial of a number using a loop.

number=int(input("Enter any number : " ))
def calculatefactorial(num):

    if num>=0:
        fact = 1
        for i in range(1,num+1):
            fact=fact*i
        return fact
    else:
        return "Given number is negative ! Negative number does not have factorial"

print(calculatefactorial(number))