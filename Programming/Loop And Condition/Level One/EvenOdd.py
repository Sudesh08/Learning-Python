#
# 1. Even or Odd Checker
# Write a function that takes a number as input and prints whether it is even or odd.

num=int(input("Enter a number to check weather it is even or odd: "))
def checkOddOrEven(number):
    if number%2==0:
        return True
    else:
        return False

if checkOddOrEven(num):
    print("The given number is Even Number")
else:
    print("The given number is Odd Number")



#
# 20. Find GCD of Two Numbers
# Write a function that finds the greatest common divisor (GCD) of two numbers using a loop and conditions.


# 1. Find All Duplicates in a List
# Write a function that returns all duplicate elements in a list of integers.
#
# 2. Check if a Number is Strong
# A Strong number is one whose sum of the factorials of digits equals the number itself (e.g., 145 = 1! + 4! + 5!). Write a function to check this.
#
# 3. Matrix Transpose
# Write a function that takes a 2D list (matrix) and returns its transpose using nested loops.
#
# 4. Find Second Largest Number in a List
# Create a function that finds the second largest number in a list without using built-in sort functions.
#
# 5. Password Strength Checker
# Write a function that checks whether a password is strong: at least 8 characters, includes uppercase, lowercase, digits, and a special character.
#
# 6. Check Happy Number
# A number is happy if repeatedly replacing it with the sum of the squares of its digits eventually results in 1. Write a function to determine if a number is happy.
#
# 7. Pattern Printer: Diamond
# Write a function to print a diamond pattern using * for a given odd number input n (rows).
#
# Example (for n = 5):
#
# markdown
# Copy
# Edit
#   *
#  ***
# *****
#  ***
#   *
# 8. Find All Palindromic Substrings in a String
# Write a function that finds and returns all substrings in a string that are palindromes.
#
# 9. Flatten a Nested List
# Write a function that takes a nested list (e.g., [1, [2, 3], [4, [5]]]) and returns a flattened version: [1, 2, 3, 4, 5].
#
# 10. Calculate LCM (Least Common Multiple)
# Write a function to compute the least common multiple of two numbers using loops and GCD.
#
#
# 1. Sudoku Solver
# Write a function to solve a valid 9x9 Sudoku puzzle using backtracking.
#
# 2. Longest Substring Without Repeating Characters
# Given a string, write a function that returns the length of the longest substring without repeating characters.
#
# 3. Knapsack Problem (0/1)
# Implement the 0/1 Knapsack algorithm using recursion and dynamic programming.
#
# 4. Find All Permutations of a String/List
# Write a function that returns all permutations of a given string or list using recursion and loops.
#
# 5. Maze Solver (Backtracking)
# Write a function to solve a maze represented by a matrix (0 = wall, 1 = path) using backtracking.
#
# 6. Word Ladder (Shortest Transformation)
# Given two words and a dictionary, find the shortest transformation sequence from start to end, changing only one letter at a time.
#
# 7. Find Maximum Subarray (Kadane’s Algorithm)
# Write a function to find the contiguous subarray within an array that has the largest sum.
#
# 8. *Expression Evaluator (with +, -, , /)
# Create a function that evaluates a mathematical expression given as a string (like "3 + 5 * (2 - 8)") using stacks.
#
# 9. N-Queens Problem
# Write a function to place N queens on an N×N chessboard such that no two queens attack each other. Use recursion and backtracking.
#
# 10. Trapping Rain Water
# Given an array of integers representing heights, calculate how much water can be trapped after rain.

