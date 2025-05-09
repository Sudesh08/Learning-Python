# 12. Print All Prime Numbers in a Range
# Create a function that takes two numbers and prints all prime numbers between them using nested loops.

def checkNumberIsPrimeOrNot(num):
    if num <= 1:
        return False  # 0 and 1 are not prime

    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False  # Not a prime number
    return True  # Prime number

range1=int(input("Enter starting range "))
range2=int(input("Enter Ending Range"))
listOfPrimeNumber=[]
for i in range(range1,range2):
    if checkNumberIsPrimeOrNot(i):
        listOfPrimeNumber.append(i)

if listOfPrimeNumber:
    print("Prime Number between range is : ",*listOfPrimeNumber)
else:
    print("Prime number doesnot present in between the range")