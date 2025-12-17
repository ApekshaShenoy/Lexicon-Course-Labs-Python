"""
5. Overriding a Method and Calling the Parent  
Create a base class with a method that prints a message.  
Override this method in a subclass.  
Inside the overridden method, call the parent version using super() and then add 
additional behavior.  
Call the method and show both outputs. 
"""
class Location:
    def message(self):
        print("I live in Sweden")

class City(Location):
    def message(self):
        super().message()  
        print("in Stockholm")

my_loc = City()
my_loc.message()
