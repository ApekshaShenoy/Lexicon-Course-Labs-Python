"""
5. Create a class that builds its string using a comprehension. Write a class whose 
__str__ method constructs its output using a comprehension and join().  

"""
class FoodOrder:
    def __init__(self, name, food, drink):
        self.name = name
        self.food = food
        self.drink = drink

    def __str__(self):
       return " , ".join(f"{key}={value}" for key,value in self.__dict__.items())
    
order = FoodOrder("Apeksha", "Fish and Chips", "Coke Zero")
print(order)
