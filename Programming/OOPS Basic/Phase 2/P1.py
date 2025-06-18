# 🔸 1. Student Grade Calculator
# Question:
# Create a class Student with attributes: name, marks (a list of 5 subject marks).
# Add methods to:
# Calculate total marks
# Calculate average marks
# Display grade (A, B, C, Fail based on average)

class Calculator:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculateTotalMarks(self):
        totalMarks=0
        for i in self.marks:
            totalMarks=totalMarks+i
        return totalMarks
    def calculateAverage(self):
        averageMarka=self.calculateTotalMarks()/len(self.marks)
        if averageMarka>=90:
            print(f"Your average marks is : {averageMarka} and your grade is A")
        elif averageMarka>=75:
            print(f"Your average marks is : {averageMarka} and your grade is B")
        elif averageMarka>=60:
            print(f"Your average marks is : {averageMarka} and your grade is C")
        else:
            print(f"Your average marks is : {averageMarka} and you are fail")

calculator1=Calculator("Sudesh",[10,18,90])
# calculator1.calculateTotalMarks()
calculator1.calculateAverage()


# 🔸 4. Temperature Converter
# Question:
# Create a class Temperature with a method:
#
# to_celsius(fahrenheit)
#
# to_fahrenheit(celsius)
#
# Use self correctly and demonstrate conversion for both.
#
# 🔸 5. Employee Salary with Bonus
# Question:
# Create a class Employee with attributes: name, base_salary.
# Add a method calculate_total_salary(bonus_percentage) that returns total salary after bonus.