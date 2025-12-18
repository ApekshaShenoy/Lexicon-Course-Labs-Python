"""
LAB 3 — EAFP vs LBYL 
Objective 
Practice EAFP-style error handling. 
Instructions 
1. Write a function that: 
o performs an operation on two inputs 
o may fail depending on the inputs 
2. Implement it using: 
o try 
o except 
3. Test the function with: 
o valid inputs 
o invalid inputs 
o edge cases 
Constraints 
• Do NOT use isinstance 
• Do NOT pre-check types

"""
def divide(a, b):
    try:
        result = a / b
        print(f"{a} divided by {b} is {result}")
    except Exception as e:
        print(f"Error: {e}")

divide(10, 2)   
divide(10, 0)   
divide("10", 2)
divide(0, 5)   
divide(5, -1)   
