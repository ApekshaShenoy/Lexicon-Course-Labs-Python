"""
Task 7: Preserving function metadata 
Create a decorator that wraps a function. 
Ensure that the wrapped function retains its original metadata. 
Verify this by inspecting the function’s name and documentation before and after 
decoration.
"""
import functools

def MyDecor(func):
    @functools.wraps(func)  
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

@MyDecor
def find_Square(num):
    """finds the square"""
    return num * num

print(find_Square.__name__)
print(find_Square.__doc__)

print(find_Square(10))