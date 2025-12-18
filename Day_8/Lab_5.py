"""
LAB 5 — Feel the Pain of isinstance 
Objective 
Recognize why type-check chains do not scale. 
Instructions 
1. Write a function that: 
o accepts an object 
o behaves differently depending on the object’s type 
o uses isinstance 
2. Add a new class that should be supported. 
3. Identify all places that must be modified. 
4. Redesign the solution using polymorphism so: 
o new classes require no changes to existing functions 
"""
class Car:
    def move(self):
        return "Car drives on the road"

class Aeroplane:
    def move(self):
        return "Aeroplane flies in the sky"

class Ship:
    def move(self):
        return "Ship sails on water"
    
class Bicycle:
    def move(self):
        return "Bicycle pedals on the street"

def start_moving(obj):
    print(obj.move())

vehicles = [Car(),Aeroplane(),Ship(),Bicycle()]
for v in vehicles:
    start_moving(v)