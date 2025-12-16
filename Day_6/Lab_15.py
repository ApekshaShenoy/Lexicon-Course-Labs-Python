"""
15. Build a formatted string using a comprehension. Generate a formatted string 
from object or dictionary data using comprehension and join().  

"""

person = {"name": "Apeksha", "age": 32, "city": "Stockholm"}

Formated_string = "\n".join(f"{key}={value}" for key,value in person.items())

print(Formated_string)