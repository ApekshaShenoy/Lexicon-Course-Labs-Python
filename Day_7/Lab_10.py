"""
10. Design Task – Controlled Inheritance Design a small inheritance hierarchy that models a real-world concept. 
Requirements: 
- Use inheritance and super() correctly 
- Override at least one method 
- Include at least one class variable
- Include either a protected or private attribute 
-Do not use polymorphism or duck typing Create objects and demonstrate that the inheritance structure works as intended.
"""

class Person:
    Species = "Human"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def information(self):
        return f"{self.name} is {self.age} years old."
    
class Person_Details(Person):
    def __init__(self, name, age, address, person_number):
        super().__init__(name, age)
        self.address = address
        self._person_number = person_number

    def information(self):
        original_info = super().information()
        return (
            f"{original_info}\n"
            f"Lives in {self.address}\n"
            f"Personal number: {self._person_number}"
        )

class BankId(Person):
    def __init__(self, name, age, bankid_pin):
        super().__init__(name, age)
        self.__bankid_pin = bankid_pin

    def information(self):
        original_info = super().information()
        return f"{original_info}\nBankID is registered"
  
person1 = Person("Apeksha", 32)
person2 = Person_Details("Apeksha", 32, "Stockholm", "123456-1234")
person3 = BankId("Apeksha", 32, 1234)

print(person1.information())
print()
print(person2.information())
print()
print(person3.information())
print()
print("Species:", Person.Species)
