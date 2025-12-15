"""
2. Create a class with a clean __str__ representation. Create a class with at least 
three attributes and implement __str__ to make printed objects readable and 
nicely formatted.  
"""
class FoodOrder:
    def __init__(self, name, food, drink):
        self.name = name
        self.food = food
        self.drink = drink

    def __str__(self):
        return f"{self.name} will have {self.food} and {self.drink}"
    

order1 = FoodOrder("Apeksha", "Fish and Chips", "Coke Zero")
order2 = FoodOrder("Mishika", "Grilled Chicken", "Milk")
order3 = FoodOrder("Srinivas", "Fish and Chips", "Pepsi Max")

print(order1)
print(order2)
print(order3)
