# Swap Three Variables
# Swap values of three variables a, b, and c in a circular way (a → b, b → c, c → a).


a= int(input("Enter 1st number: "))
b= int(input("Enter 2nd number: "))
c= int(input("Enter 3rd number: "))
print("Before swapping : a: ",a," b: " ,b, " c: ",c)
temp=a
a=b
b=c
c=temp

print("After swapping : a: ",a," b: " ,b, " c: ",c)