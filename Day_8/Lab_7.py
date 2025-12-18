"""
LAB 7 — Duck Typing vs ABCs (Comparison Lab) 
Objective 
Compare flexibility vs safety. 
Instructions 
1. Solve the same problem twice: 
o once using duck typing 
o once using an abstract base class 
2. Intentionally violate the expected interface in both versions. 
3. Compare: 
o error timing 
o error messages 
o developer experience
"""
"""
# Duck typing
class Car:
    def move(self):
        return "Car drives on the road"

class Ship:
    def move(self):
        return "Ship sails on water"

class BrokenTransport:
    pass

def start_moving(obj):
    print(obj.move())

start_moving(Car())   
start_moving(Ship())
start_moving(BrokenTransport())  #throws run time error
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

class BrokenTransport(ModeOfTransport):
    pass

def start_moving(obj: ModeOfTransport):
    print(obj.move())

start_moving(Car())   
start_moving(Ship())
broken = BrokenTransport()
