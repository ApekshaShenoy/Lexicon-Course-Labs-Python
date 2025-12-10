"""
LAB 5 — Username Generator 
Ask the user for: 
• First name 
• Last name 
• Birth year 
Then generate a username using slicing, for example: 
first 2 letters of first name + last 3 letters of last name + last 2 digits of birth year 
Goal: Combine indexing, slicing, formatting, variables. 
"""

first_name = input("Enter your first name:").strip()
last_name = input("Enter your last name:").strip()
birth_year = input("Enter your birth year:").strip()

user_name = first_name[:2] + last_name[-3:] + birth_year[-2:]
print(f"Username: {user_name}")