"""
6. Implement __eq__. Create a class where two objects are equal if their attributes 
match.
"""
class info:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self,other):
        if not isinstance(other,info):
            return False
        
        return (self.name == other.name and self.age == other.age)
    

p1 = info("Apeksha",32)
p2 = info("Apeksha",32)
p3 = info("Apeksha",28)

print(p1 == p2) 
print(p1 == p3) 