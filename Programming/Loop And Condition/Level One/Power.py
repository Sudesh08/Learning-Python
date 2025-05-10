# 18. Calculate Power (Exponentiation)
# Write a function that takes a base and exponent and calculates the result using a loop (not the ** operator).

def findPower(b,e):
    power=1
    if e>=0:
        for i in range(e):
            power=power*b
        return power
    else:
        for i in range(-e):
            power *= b
        power = 1 / power
        return power


base=int(input("Enter Base : "))
exponent = int(input("Enter Exponent : "))
print(findPower(base,exponent))