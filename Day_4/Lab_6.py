"""
6. Using nonlocal
Create an example where an inner function modifies a variable in the enclosing function using the
nonlocal keyword. Show the change before and 
"""
Location = "global"

def outer_func():
    Location= "outer function"
    print(f"Before inner function:{Location}")

    def inner_func():
        nonlocal Location
        Location = "inner function"
        print(f"Inside inner function:{Location}")

    inner_func()
    print(f"After inner function:{Location}")

outer_func()
print(f"In global scope :{Location}")