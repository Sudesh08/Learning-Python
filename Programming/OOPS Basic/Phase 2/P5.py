#
# 🔸 5. Employee Salary with Bonus
# Question:
# Create a class Employee with attributes: name, base_salary.
# Add a method calculate_total_salary(bonus_percentage) that returns total salary after bonus.

class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    def calculate_total_salary(self,bonus_percentage):
        totalSalary=(self.base_salary*bonus_percentage/100)+self.base_salary
        return totalSalary

employee1=Employee("Sudesh",50000)
print(employee1.calculate_total_salary(5))