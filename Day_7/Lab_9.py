"""
9. Overriding __str__ in a Subclass  
Create a base class with a meaningful __str__ method.  
Override __str__ in a subclass.  
Use super().__str__() inside the subclass and add subclass-specific information.  
Print objects of both classes to show the diAerence.  

"""
class Family:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
class Details(Family):
    def __init__(self, name, age,gender):
        super().__init__(name, age)
        self.gender = gender

    def __str__(self):
        family_str = super().__str__()
        return f"{family_str} and {self.gender}"
    
p2 = Details("Apeksha", 32, "Female")
print(p2)


    