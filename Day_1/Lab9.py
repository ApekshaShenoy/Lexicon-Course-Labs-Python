"""
LAB 9 — List Comprehension Transformations 
Given: 
numbers = [1,2,3,4,5,6,7,8,9] 
Students must create using list comprehensions: 
1. A list of squares 
2. A list of only even numbers 
3. A list of numbers doubled 
4. A list of only numbers greater than 5 
5. A list of strings: "Number: X" for each element 
Goal: Become comfortable with comprehensions. 
"""

numbers = [1,2,3,4,5,6,7,8,9]

squares = [n*n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
doubled = [n*2 for n in numbers]
greater_than_5 = [n for n in numbers if n > 5]
strings = [f"Number: {n}" for n in numbers]

print(squares)
print(evens)
print(doubled)
print(greater_than_5)
print(strings)
