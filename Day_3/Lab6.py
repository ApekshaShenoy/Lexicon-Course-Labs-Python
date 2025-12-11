"""
LAB 6 — Even Number Filter Tool (Mini Project)
1. Accept a line of numbers from the user
2. Convert input into a list of integers
3. Use filter() + lambda to keep only even numbers
4. Print the even-number list and the count
"""

# 1
my_input = input("Enter the numbers separated by space: ")

# 2
my_numbers = [int(num) for num in my_input.split()]

# 3
even_numbers = list(filter(lambda num: num % 2 == 0, my_numbers))

# 4
print("Even numbers:", even_numbers)
print("Count of even numbers:", len(even_numbers))
