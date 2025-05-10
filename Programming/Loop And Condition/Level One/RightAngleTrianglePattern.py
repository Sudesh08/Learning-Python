# 17. Print Triangle Pattern
# Create a function that takes a number n and prints a right-angled triangle pattern of stars (*) using nested loops.

# *
# **
# ***
# ****

def printTrianglePattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

    # for i in range(1, n + 1):
    #     print("*" * i)

# Get user input
num = int(input("Enter number of rows: "))
printTrianglePattern(num)

