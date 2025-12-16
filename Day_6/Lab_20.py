"""20. Combine kwargs, property, and a dunder method. Create a class that: - accepts 
all attributes via **kwargs - includes at least one property with getter and setter - 
implements one or more dunder methods - includes a method that performs a 
calculation using its data 
"""
class Student:
    def __init__(self, **kwargs):
        for key,value in kwargs.items():
            setattr(self , key , value)


    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self,value):
        if value < 0 :
            raise ValueError("Marks cannot be negative")
        self._marks = value

    def has_passed(self):
        return self.marks >= 40
    
    def __str__(self):
        return "\n".join(f"{key} = {value}" for key, value in self.__dict__.items())
    

s1 = Student(name="Apeksha", subject="Python")
s1.marks = 72

print(s1)
print("Passed:", s1.has_passed())
     