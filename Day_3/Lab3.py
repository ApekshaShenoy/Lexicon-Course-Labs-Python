"""
LAB 3 — Functions & Conditionals 
Create functions that: 
1. Return a greeting with a name 
2. Return a default greeting if no name is given 
3. Check if a number is even 
4. Add two numbers only if both are even, otherwise return 0 
Goal: Practice function creation, return values, and conditional logic
"""
# 1 & 2: 

def greet(name="Apeksha"):
    if not name:  
        name = "Apeksha"
    return f"Good Morning {name}, Have a great day!!"

my_name = input("Enter your name: ")
print(greet(my_name))

#3
def addition(a, b):
    if a % 2 != 0 or b % 2 != 0:
        return 0
    else:
        total = a + b
        print(f"Sum: {total}")
        return total

my_number1 = int(input("Enter your number 1: "))
my_number2 = int(input("Enter your number 2: "))

# even number
if my_number1 % 2 == 0:
    print(f"{my_number1} is even")
else:
    print(f"{my_number1} is odd")

add_2 = addition(my_number1,my_number2)
print(f"Add only if both numbers are even. Sum of {my_number1} and {my_number2} is :{add_2}")
