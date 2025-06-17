# ✅ 1. Create a class to represent a student
# Question:
# Write a class Student that has attributes: name, roll_number. Add a method to display the student details.
#
# # Expected output:
# # Name: Sudesh
#  Roll Number: 101




class Student:
    # Constructor
    def __init__(self,name,rollnNo,age):
        self.name = name
        self.age = age
        self.rollNO=rollnNo
    def greeting(self):
        print(f"Hello guyz Good Morning! My name is {self.name} my age is {self.age} and my rollNO is {self.rollNO}")

student1= Student("Sudesh Mahato","001",25)
student1.greeting()

student2=Student("Darshan","002",24)
student2.greeting()