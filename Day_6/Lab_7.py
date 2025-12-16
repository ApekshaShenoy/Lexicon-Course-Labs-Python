"""
7. Implement __lt__. Create a class where objects can be compared using < based 
on one chosen attribute. 

"""

class PriceCompare:
    def __init__(self,shop_product,price):
        self.shop_product = shop_product
        self.price = price

    def __lt__(self ,other):
        if not isinstance(other ,PriceCompare):
            return NotImplemented
        return self.price < other.price
    

p1 = PriceCompare("willys:bread",25)
p2 = PriceCompare("Ica:bread",35)

print(p1 < p2)
print(p2 < p1)