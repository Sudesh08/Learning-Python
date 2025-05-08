# 7. Sum of Even Numbers in a Range
# Write a function that takes a start and end number and returns the sum of all even numbers in that range.




def sumOfPrimeNumBetweenRange(num1,num2):
    Add = 0
    for i in range(num1 + 1, num2):
        if i % 2 == 0:
            Add = Add + i
    return Add

number1=int(input("Enter staring number"))
number2=int(input("Enter ending number"))
print(sumOfPrimeNumBetweenRange(number1,number2))
