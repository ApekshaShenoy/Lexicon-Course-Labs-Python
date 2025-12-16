"""
16. Create a nested comprehension. Generate a two-dimensional structure (like a 
table or grid) with nested comprehensions. SECTION 4 — Combined OOP + 
Scope + Pythonic Techniques

"""

stars = [["*" for _ in range(3)] for _ in range(3)]

for row in stars:
    print(" ".join(row))



