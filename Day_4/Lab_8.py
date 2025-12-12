"""
8. Class Attribute vs Instance Attribute
Create a program demonstrating a class attribute shared across multiple objects. Then change the
attribute for only one object and show that the other objects still use the original class attribute.
"""
class Laptop:
    brand = "Dell"

    def __init__(self, model):
        self.model = model
        
lap1 = Laptop("Inspiron")
lap2 = Laptop("XPS")

print(f"lap1 brand: {lap1.brand}, model: {lap1.model}")
print(f"lap2 brand: {lap2.brand}, model: {lap2.model}")

lap1.brand = "HP"   

print(f"lap1 brand after change: {lap1.brand}, model: {lap1.model}")
print(f"lap2 brand remains: {lap2.brand}, model: {lap2.model}")
