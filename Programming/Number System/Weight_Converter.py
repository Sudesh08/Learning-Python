# BMI Calculator
# Ask user for weight (kg) and height (meters), then calculate BMI.

user_Weight=float(input("Enter user weight in kg : "))

user_Height=float(input("Enter user height in m : "))
def calculateBMI(weight,height):
    return weight/(height*height)

print(calculateBMI(user_Weight,user_Height))
