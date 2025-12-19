"""
Task 2: Functional list transformation 
Use a functional approach to transform a list of numbers. 
Apply one operation that changes the values and one operation that filters values. 
The solution must use lambda expressions together with built-in higher-order functions.

"""
my_list = [1,2,3,4,5,6,7,8,9,10,11,12]

double = map(lambda x: x * x, my_list)

odds = list(filter(lambda x: x % 2 != 0 , double))

print(odds)




