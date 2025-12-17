"""
7. Protected Attributes  
Create a base class that uses a protected attribute (single underscore).  
Access and modify this attribute from a subclass.  
Demonstrate that the attribute can be accessed, and explain why this is allowed but 
discouraged outside the class hierarchy. 

"""
class Person:
    def __init__(self,name, age):
        self.name = name
        self._age = age

class Family(Person):
    def Birthday(self):
        self._age += 1
        print("Happy {}'rd Birthday {}".format(self._age , self.name))

a = Family("Apeksha",32)
a.Birthday()
print("Accessing protected attribute directly:", a._age)