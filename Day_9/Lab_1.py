"""
Task 1: Execution-time decorator 
Create a decorator that measures how long a function takes to execute. 
The decorator should print the execution time after the function has finished. 
Apply the decorator to a function that processes a list of numbers.
"""
import time

def ExecutionTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time needed for the fuction execution:",end-start)
        return result
    return wrapper

@ExecutionTime
def Odd_square():
    for num in range(1,15):
        if num % 2 != 0:
            result = num * num
            print(result)
    return result

Odd_square()

