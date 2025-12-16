"""
9. Implement __len__. Create a class where len(object) returns a meaningful 
numeric value based on internal data. 

"""
class Cart:
    def __init__(self,items):
      self.items = items

    def __len__(self):
       return len(self.items)
    

P1 = Cart(["mikk","bread","bregott","cheeese","eggs"])
print(len(P1))