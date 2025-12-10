"""
LAB 4 — String Methods Investigation 
Using a string from user input, students must show: 
1. Uppercase version 
2. Lowercase version 
3. How many characters the string has 
4. Split the string into words 
5. Replace one letter with another 
Goal: Practice built-in string methods & transformations.
"""

my_string = input("Enter your string:")

print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Length:", len(my_string))
print("Split:", my_string.split())
print("Replace one letter:", my_string.replace("a", "x"))