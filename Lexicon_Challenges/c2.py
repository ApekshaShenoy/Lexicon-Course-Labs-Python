"""
Challenge 2 – Class With Both Class-Level and Instance-Level Behavior
Write a class that uses:- at least one class attribute- at least one instance attribute- at least one method that uses the class attribute- at least one method that uses only the instance attributes
Then add a way to change the class attribute and show how this affects all existing objects. Also show
how changing an instance attribute affects only one object
"""
class Employee:
    company = "TechCorp"   

    def __init__(self, name, salary):
        self.name = name          
        self.salary = salary      

    def show_company(self):
        return f"{self.name} works at {Employee.company}"

    def annual_salary(self):
        return self.salary * 12

e1 = Employee("Apeksha", 3000)
e2 = Employee("Srinivas", 4000)

print(e1.show_company())
print(e2.show_company())

Employee.company = "NewTech"

print(e1.show_company())
print(e2.show_company())

e1.salary = 3500

print(e1.annual_salary())
print(e2.annual_salary())
