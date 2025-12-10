"""
8. Tuple with Condition
Create a new tuple that contains only the even numbers from a given tuple of integers.
"""
mytuple = (1, 2, 3, 5, 6, 7, 8, 9, 10)

#for i in mytuple:
#   if i % 2 == 0:
#       my_even_tuple += (i,) 

my_even_tuple = tuple(i for i in mytuple if i % 2 == 0)

print("Tuple with only even numbers:", my_even_tuple)
