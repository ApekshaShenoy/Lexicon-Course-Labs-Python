"""
LAB 2 — Break Duck Typing on Purpose 
Objective 
Understand the risk of duck typing. 
Instructions 
1. Take your function from Lab 1. 
2. Pass an object that does not implement the expected behavior. 
3. Observe the error. 
4. Explain: 
o when the error occurs
"""
class ModeOfTransport:
    def move(self):
        return "Moves"

class Aeroplane(ModeOfTransport):
    def move(self):
        return "goes in the sky"

class Car(ModeOfTransport):
    def move(self):
        return "goes on the road"

class Ship(ModeOfTransport):
    def move(self):
        return "goes on water"

class Bicycle:
    def pedal(self):
        return "Pedaling fast"

def start_moving(obj):
    print(obj.move())

vehicles = [Aeroplane(), Car(), Ship(),Bicycle()]

for v in vehicles:
    start_moving(v)
    