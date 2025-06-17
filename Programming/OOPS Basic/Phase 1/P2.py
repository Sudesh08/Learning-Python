# ✅ 2. Simple Calculator Class
# Question:
# Create a class Calculator with methods to add, subtract, multiply, and divide two numbers.
# Create an object and perform operations.
#
# # Example:
# # calc = Calculator()
# # calc.add(5, 3)  # Output: 8

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2

    def divide(self):
        return self.num1/self.num2

calculate1=Calculator(1,2)
print(calculate1.sub())