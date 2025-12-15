"""
1. Create a class with a property and setter. Create a class with one attribute that 
can only be accessed and modified through a property and setter. Include a 
method that performs a calculation using the attribute. 
"""
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_balance

    def add_interest(self, rate):
        return self._balance * (1 + rate)


acc = BankAccount(100)
print(acc.balance)       
acc.balance = 50         
print(acc.add_interest(0.1))  
