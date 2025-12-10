"""
LAB 7 — Shopping Cart Program 
Simulate a shopping cart using lists. 
Steps: 
1. Start with an empty list cart = [] 
2. Ask user 5 times to input an item and append it 
3. After all items are added: 
o Print the full cart 
o Remove the last item 
o Show how many items remain 
o Print only the first and last items 
Goal: Combine lists, len(), append(), pop(), indexing. 

"""
cart = []

for i in range(5):
    item = input("Enter item: ")
    cart.append(item)

print(f"Full cart:{cart}")
print(cart.pop())
print("Number of items in the cart", len(cart))
print(f"First item is :{cart[0]} and last item is :{cart[-1]}")

