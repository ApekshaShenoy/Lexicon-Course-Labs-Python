""""
LAB 1 — Python Calculator (Numbers & Arithmetic)
Create a program that: 
1. Takes two numbers from the user 
2. Calculates and prints: 
o Sum 
o Difference 
o Product 
o Division 
o Power 
3. Print the results in a nicely formatted way. 
Goal: Practice numeric operations & print formatting.

"""
def addition(a, b):
    total = a + b
    print(f"Sum: {total}")
    return total

def subtraction(a, b):
    difference = a - b
    print(f"Difference: {difference}")
    return difference

def multiplication(a, b):
    product = a * b
    print(f"Product: {product}")
    return product

def division(a, b):
    if b == 0:
        print("Division: Cannot divide by zero")
        return None
    result = a / b
    print(f"Division: {result}")
    return result

def power(a, b):
    result = a ** b
    print(f"Power: {result}")
    return result

print("Enter two numbers:")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

print("\nResults:")
addition(num1, num2)
subtraction(num1, num2)
multiplication(num1, num2)
division(num1, num2)
power(num1, num2)



    