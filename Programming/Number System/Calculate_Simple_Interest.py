# Simple Interest Calculator
# Write a program to calculate simple interest given principal, rate, and time.

principal=float(input("Enter Principal to calculate Simple Interest: "))
rate=float(input("Enter Rate to calculate Simple Interest: "))
time=int(input("Enter Time in months to calculate Simple Interest: "))

Simple_Interest=float(((principal * rate * time ) / (12*100)))

print("Simple interest of " , Simple_Interest)