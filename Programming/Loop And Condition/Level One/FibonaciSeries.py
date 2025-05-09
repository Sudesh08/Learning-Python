#
# 10. Fibonacci Series Generator
# Create a function that prints the first n numbers of the Fibonacci series using a loop.

def findFibonacciSeries(n):
    n1 = 0
    n2 = 1
    series=[]

    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        series.append(n1)
        # print(n1)
    else:
        # print(n1)
        # print(n2)
        series.append(n1)
        series.append(n2)
        for i in range(2, n):
            n3 = n1 + n2
            series.append(n3)
            # print(n3)
            n1 = n2
            n2 = n3
    print(*series)

nNumber = int(input("Enter nth term to find Fibonacci series: "))
findFibonacciSeries(nNumber)
