# ✅ 3. Create multiple objects of a class
# Question:
# Create a class Car with attributes brand and price. Create 3 different objects and print their details.

class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def printDetails(self):
        print(f"Brand of the Car is : {self.brand}")
        print(f"Price of the Car is : {self.price}")

car1=Car("Honda","12Lac")
car1.printDetails()
print("-----------------------------------")
car2=Car("Tata","26Lac")
car2.printDetails()
print("-----------------------------------")
car3=Car("Sizuki","15Lac")
car3.printDetails()
