"""
Task 3: Closure-based configuration 
Create a function that returns another function. 
The returned function should behave differently depending on a value captured from the 
outer function. 
Create at least two functions from the same factory function and demonstrate the difference 
in behavior.
"""
def multiplication(number):
    def mutiply(num):
        return num * number
    return mutiply

result1 = multiplication(5)
result2 = multiplication(6)

print(result1(10))
print(result2(10))