"""
Challenge 1 – Tracking Variable Changes Across Scopes
Create a program that uses three nested functions. Each function should have a variable with the same
name but different values. Use print statements to show exactly which value is used at each level, and
experiment with both nonlocal and global to change the outcome

"""
x = "GLOBAL"

def outer():
    x = "ENCLOSING"

    def middle():
        nonlocal x
        x = "MODIFIED BY NONLOCAL"

        def inner():
            global x
            x = "MODIFIED BY GLOBAL"
            print("Inner x:", x)

        inner()
        print("Middle x:", x)

    middle()
    print("Outer x:", x)

outer()
print("Global x:", x)
