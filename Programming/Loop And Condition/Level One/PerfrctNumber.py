# 16. Check Perfect Number
# Write a function to check if a number is perfect (sum of its divisors excluding itself equals the number).

def isPerfectNumber(n):
    add=0
    for i in range(1,n//2+1):
        if n%i==0:
            add=add+i
    return add==n



num=int(input("Enter a number to check weather it is perfect or not : "))
print("Given Number is Perfect number "if isPerfectNumber(num) else "Not a perfect number")
