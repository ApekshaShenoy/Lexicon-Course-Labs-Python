"""
LAB 5 — *args and kwargs 
Create functions that: 
1. Accept any number of values using *args and return their sum 
2. Accept any number of values using *args and return the maximum 
3. Accept any number of keyword arguments using **kwargs and print them 
4. Combine a, *args, and **kwargs and print all arguments in a readable way 
Goal: Practice flexible function parameters and argument unpacking. 
"""

# 1: 
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total


# 2: 
def max_value(*args):
    if not args:     
        return None
    maximum = args[0]
    for num in args:
        if num > maximum:
            maximum = num
    return maximum


# 3: 
def print_kwargs(**kwargs):
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(key, ":", value)


# 4
def combined(a, *args, **kwargs):
    print("a:", a)

    print("args:", args)

    print("kwargs:")
    for key, value in kwargs.items():
        print(key, ":", value)


print("Sum:", sum_values(1, 2, 3, 4, 5))
print("Max value:", max_value(10, 2, 45, 3))

print_kwargs(name="Apeksha", city="Stockholm", role="Student")

combined(10, 20, 30, 40, name="Apeksha", country="Sweden")
