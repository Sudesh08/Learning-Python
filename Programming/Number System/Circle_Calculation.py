# Circle Calculations
# Input the radius and calculate both the area and circumference of the circle.

#c = 2πr and A = πr²

radius= float(input("Enter Radius of the circle: "))
piValue=float(3.14159265359)

def calculate_Circumference(r):
    return 2*piValue*r

def calculate_Area(r):
    return piValue*r*r

print("Circumference of circle : ",calculate_Circumference(radius))


print("Area of circle : ",calculate_Area(radius))

