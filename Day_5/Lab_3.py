"""
3. Create a class with a meaningful __repr__. Create a class where __repr__ returns 
a string that could realistically recreate the object. 

"""
class FoodOrder:
    def __init__(self, name, food, drink):
        self.name = name
        self.food = food
        self.drink = drink

    def __repr__(self):
        return f"FoodOrder({self.name!r}, {self.food!r}, {self.drink!r})"
    
order1 = FoodOrder("Apeksha", "Fish and Chips", "Coke Zero")
order2 = FoodOrder("Mishika", "Grilled Chicken", "Milk")
order3 = FoodOrder("Srinivas", "Fish and Chips", "Pepsi Max")

print(order1)
print(order2)
print(order3)