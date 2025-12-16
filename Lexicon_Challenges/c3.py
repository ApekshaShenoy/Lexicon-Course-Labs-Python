"""
Challenge 3 – Object Interaction
Create two different classes where objects from one class interact with objects from the other.
Demonstrate how these interactions work and how changing attributes in one object affects the result in
the other
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(p.price for p in self.products)

p1 = Product("Milk", 20)
p2 = Product("Bread", 15)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

print("Total:", cart.total_price())

p1.price = 25

print("Total after price change:", cart.total_price())
