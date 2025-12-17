"""
3. Multiple Inheritance and MRO  
Create two parent classes that both modify the same attribute in their constructors.  
Create a child class that inherits from both parents.  
Use super() in all constructors.  
Print the final value and print the MRO of the child class.  
Explain why the final value is produced.

"""
class Cookie:
    def __init__(self, value):
        self.value = value
        print(f"Initial cookies: {self.value}")

class Mom(Cookie):
    def __init__(self, value):
        super().__init__(value)
        self.value -= 1
        print(f"After mom eats 2 cookie: {self.value}")

class Dad(Cookie):
    def __init__(self, value):
        super().__init__(value)
        self.value -= 4
        print(f"After dad eats 4 cookies: {self.value}")

class Child(Mom, Dad):
    def __init__(self, value):
        super().__init__(value)
        print(f"Child counts remaining cookies: {self.value}")

cookies = Child(15)

print("Remaining cookies:", cookies.value)
print("MRO:", Child.mro())

