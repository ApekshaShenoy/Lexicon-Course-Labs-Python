"""
LAB 4 — Filter & Lambda Functions 
Create programs that: 
1. Use filter() + a function to keep only even numbers 
2. Use filter() + lambda to keep only even numbers 
3. Filter names that have 3 or more characters 
4. Filter words that contain the letter "a" 
Goal: Practice the filter() function and lambda expressions. 
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1
def is_even(number):
    return number % 2 == 0

even_list1 = list(filter(is_even,numbers))
print("Even number list using filter() and function",even_list1)

# 2
even_list2 = list(filter(lambda num: num % 2 == 0,numbers))
print("Even number list using filter() and lamda",even_list2)

# 3
my_names = ["Anna","Jo","Matilda","Pelle"]

Name_3 = list(filter(lambda name: len(name)>= 3 , my_names))
print(f"Names with 3 or more character:{Name_3}")

#4
Name_a = list(filter(lambda name: "a" in name,my_names))
print(f"Names with \"a\" in it:{Name_a}")

