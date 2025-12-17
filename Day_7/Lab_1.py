"""
Inheritance & OOP – Exercise Set  
1. Constructor Execution Order  
Create a base class and two subclasses that form an inheritance chain.  
Each class must print a message from its constructor.  
Create an object of the most derived class and observe the order in which the 
constructors are executed.  
Use super() in all constructors.  

"""
class Europe:
    def __init__(self):
        print("Europe constructor called")

class Sweden(Europe):
    def __init__(self):
        super().__init__()
        print("Sweden Constructor called")

class Stockholm(Sweden):
    def __init__(self):
        super().__init__()
        print("Stockholm constructor called")

city = Stockholm()