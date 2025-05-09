# 2. Find Maximum of Three Numbers
# Create a function that takes three numbers and returns the largest one using conditional statements.

number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
number3=int(input("Enter third number: "))

def maximumNumberAmongThree(num1,num2,num3):
    if num1>num2 and num1>num3:
        return f"{num1} is greater"
    elif num2>num1 and num2>num3:
        return f"{num2} is greater"
    elif num3>num1 and num3>num2:
        return f"{num3} is greater"
    else:
        return f"{num1,num2,num3} is equal"

print(maximumNumberAmongThree(number1,number2,number3))