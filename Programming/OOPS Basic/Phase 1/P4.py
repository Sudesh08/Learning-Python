# ✅ 4. Add a method to update object data
# Question:
# Create a class Employee with attributes name and salary. Add a method update_salary(new_salary)
# to change the salary of the employee.
# # Example:
# # emp = Employee("Ravi", 30000)
# # emp.update_salary(35000)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def updateSalary(self,newSalary):
        print("Previous salary is",self.salary)
        self.salary=newSalary

employee1=Employee("Sudesh",40000)
employee1.updateSalary(1000)
print(f"New Salary : {employee1.salary}")

