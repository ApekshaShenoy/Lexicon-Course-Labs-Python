"""
2. Function Using a Global Variable
Write a function that reads the value of a global variable without changing it. Show in the output that the
global value remains the same after the function call.
"""
counter = 10

def show_counter():
    print(f"Reading the global variable: {counter}")  # Global 

show_counter()
print(f"Value outside the function (global): {counter}")

