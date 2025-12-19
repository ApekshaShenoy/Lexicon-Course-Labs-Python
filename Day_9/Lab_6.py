"""
Task 6: Higher-order function pipeline 
Create a function that takes another function as input. 
Chain multiple function calls together to process a value step by step. 
Use both named functions and lambda expressions in the pipeline.

"""

def square(a):
    return a * a
    
def sqrt(a):
    return a ** 0.5  
    
def pipeline(value,funcs):
    result = value

    for func in funcs:
        result = func(result)
    return result

functions = [square,
            lambda x : x / 0.5,
            lambda x: x * x,
            sqrt,
            ]

result = pipeline(10, functions)
print(result)