"""
8. Private Attributes and Name Mangling  
Create a base class with a private attribute using double underscores.  
Attempt to access the attribute directly and observe what happens.  
Then access it using name mangling and explain how Python handles private 
attributes internally. 

"""
class BankId:
    def __init__(self,pin):
        self.__pin = pin

Pin = BankId(1234)
try:
    print(Pin.__balance)
except AttributeError as e:
    print("Error:", e)
print("Accessing via name mangling:", Pin._BankId__pin)