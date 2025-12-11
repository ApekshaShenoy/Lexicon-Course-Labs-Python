"""
LAB 2 — Lists & Comprehensions 
Create a program that: 
1. Takes a given list of numbers 
2. Generates and prints: 
o A list of squares using a loop 
o A list of squares using a list comprehension 
o A list of positive numbers using a comprehension 
Goal: Practice list operations, loops, and list comprehensions. 
"""
my_list = [1,2,3,4,5,6,7,8,9,10]

my_sqares1 =[]
print("Squares of the numbers using loop:")
for num in my_list:
    my_sqares1.append(num*num)
print(my_sqares1, end = " ")

print("\nSquares of the numbers using list comprehension:")
my_sqaures2 = [num*num for num in my_list]
print(my_sqaures2, end =" ")

positive_numbers = [num for num in my_list if num > 0]
print("\nPositive numbers:", positive_numbers)
