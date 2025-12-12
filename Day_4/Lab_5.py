"""
5. Inner Function and the LEGB Rule
Write a function that contains an inner function. Use print statements to show which version of a name
is being used (local, enclosing, or global).
"""
Location = "global"

def outer_func():
    Location = "outer function"
    print(f"where am I :{Location} (enclosing)")

    def inner_func():
        Location = "inner function"
        print(f"where am I :{Location} (local)")

    inner_func()
    print(f"where am I :{Location} (enclosing)")

outer_func()
print(f"where am I :{Location} (Global)")


