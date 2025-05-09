# 3. Multiplication Table Generator
# Write a function that takes a number and prints its multiplication table up to 10 using a loop.

number=int(input("Enter any number to generate table : "))
def multiplicationGenerator(num):
    for i in range(1,11):
        print(num , " x ",i," = ", num*i)

multiplicationGenerator(number)