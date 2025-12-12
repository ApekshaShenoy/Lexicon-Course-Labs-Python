"""
3. Function That Modifies a Global Variable
Write a program where a function changes the value of a global variable using the global keyword.
Display the value before and after the function call.
"""
car = "BMW"

def Brand_name():
    global car         
    car = "Audi"       
    print(f"Inside function: I have a {car}")

print(f"Before function call: {car}")

Brand_name()
print(f"After function call: {car}")
