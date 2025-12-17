"""
6. Class Variables Across Inheritance  
Create a base class with a class variable.  
Create two subclasses.  
Override the class variable in one subclass but not the other.  
Create objects from all classes and show how the value diAers depending on which 
class is used. 

"""
class Company:
    salary = 50000

    def __init__(self,name):
        self.name = name
        print(f"{self.name}'s salary is: {self.salary}")

class Gen_emp(Company):
    pass

class Cyber_sec(Company):
    salary = int(Company.salary * 1.10)


emp1 = Gen_emp("carl")
emp2 = Cyber_sec("Apeksha")