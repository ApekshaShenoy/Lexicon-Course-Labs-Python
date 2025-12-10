"""
10. List Comprehension – Even Numbers
Write a program that takes a list of integers and uses list comprehension to create a new list
containing only the even numbers.
"""
mylst = [1, 2, 3, 5, 6, 7, 8, 9, 10]

my_even_lst = [i for i in mylst if i % 2 == 0]

print("List with only even numbers:{}".format(my_even_lst))