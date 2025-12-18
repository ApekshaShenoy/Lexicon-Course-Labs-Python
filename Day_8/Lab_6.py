"""
LAB 6 — Abstract Base Class Enforcement 
Objective 
Understand why ABCs exist. 
Instructions 
1. Design an abstract base class that: 
o represents a role or capability 
o defines at least one abstract method 
2. Attempt to: 
o create a subclass that does not implement the method 
o instantiate it 
3. Observe and explain the error. 
4. Create: 
o one valid subclass 
o a second valid subclass with different behavior 
5. Write a function that: 
o accepts the abstract base class 
o calls the abstract method 
"""
from abc import ABC, abstractmethod

class ModeOfTransport(ABC):
    
    @abstractmethod
    def move(self):
        pass  

class Car(ModeOfTransport):
    def move(self):
        return "Car drives on the road"

class Ship(ModeOfTransport):
    def move(self):
        return "Ship sails on water"
    
def start_moving(obj: ModeOfTransport):
    print(obj.move())

vehicles = [Car(), Ship()]

for v in vehicles:
    start_moving(v)



