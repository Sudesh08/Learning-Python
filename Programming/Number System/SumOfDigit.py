# Sum of Digits
# Input a number and find the sum of its digits.
# Example: 123 → 1 + 2 + 3 = 6

num=int(input("Enter any number: "))
def sum_of_digit(n):
    numLength=len(str(n))
    Add=0
    for val in range(numLength):
        r=n%10
        Add=Add+r
        n=int(n/10)
    return Add


print("Sum of ",num," is: ",sum_of_digit(num))

