"""
Task 4: Decorator that modifies return values 
Create a decorator that intercepts the return value of a function. 
Modify the return value in some meaningful way before returning it. 
Apply the decorator to at least one function and demonstrate the effect. 

"""

def greet(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return f"Happy Birthday!! {result}"
    return wrapper
    
@greet
def name():
    return "Apeksha"

print(name())