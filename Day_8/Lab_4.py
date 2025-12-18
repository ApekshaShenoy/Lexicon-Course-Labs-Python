"""
LAB 4 — Build Polymorphism with Inheritance 
Objective 
Understand method overriding and runtime dispatch. 
Instructions 
1. Design a base class representing a general concept. 
2. The base class must define a method but not implement it. 
3. Create at least three subclasses that: 
o inherit from the base class 
o override the method with different behavior 
4. Write a function that: 
o accepts the base class 
o calls the method 
o does NOT use conditionals 
5. Call the function with each subclass. 
Constraints 
• Do NOT use if, elif, or isinstance 
"""
from abc import ABC, abstractmethod

class ModeOfTransport(ABC):
    @abstractmethod
    def move(self):
        pass  # No implementation here
class Aeroplane(ModeOfTransport):
    def move(self):
        return "Aeroplane flies in the sky"

class Car(ModeOfTransport):
    def move(self):
        return "Car drives on the road"

class Ship(ModeOfTransport):
    def move(self):
        return "Ship sails on water"
    
def start_moving(obj):
    print(obj.move())

vehicles = [Aeroplane(), Car(), Ship()]

for v in vehicles:
    start_moving(v)

