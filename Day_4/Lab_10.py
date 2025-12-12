"""
10. Method for Updating an Attribute
Write a class where an attribute can be updated through a custom method. Demonstrate how the
updated attribute changes the behavior of another method in the class.
"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def update_temperature(self, new_value):
        self.celsius = new_value

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

t1 = Temperature(25)

print("Initial Celsius:", t1.celsius)
print("Initial Fahrenheit:", t1.to_fahrenheit())

t1.update_temperature(30)

print("\nUpdated Celsius:", t1.celsius)
print("Updated Fahrenheit:", t1.to_fahrenheit())
