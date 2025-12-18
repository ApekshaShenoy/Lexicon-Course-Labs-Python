"""
LAB 1 — Discover Duck Typing 
Objective 
Understand that shared behavior, not shared type, enables polymorphism. 
Instructions 
1. Write a function that: 
o accepts a single argument 
o calls one method on that argument 
2. Call the function with: 
o a built-in type 
o a custom class you create yourself 
3. The function must work without modification for both. 
Constraints 
• Do NOT use isinstance 
• Do NOT check types explicitly 

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

def start_moving(obj):
    print(obj.move())

vehicles = [Aeroplane(), Car(), Ship()]

for v in vehicles:
    start_moving(v)
    
class TextWrapper:
    def __init__(self, text):
        self.text = text
    def move(self):
        return self.text.upper()

start_moving(TextWrapper("Lets Move!!"))  

