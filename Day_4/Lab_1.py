"""
1. Local vs Global Variable
Create a program that demonstrates the difference between a local variable and a global variable. The
program should clearly show both values
"""
my_name = "Apeksha"

def greet():
    my_name = "Anna"
    print(f"Hello from the function: {my_name}")

greet()
print(f"Hello from the global scope: {my_name}")

