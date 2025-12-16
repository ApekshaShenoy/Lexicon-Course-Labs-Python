"""
13. Create a filtered list comprehension. Make a comprehension that filters elements 
based on a condition. 

"""
fruits = ["Apple","Persimon","Kiwi","Blueberry"]
fruit1 = [f for f in fruits if len(f) > 7]
print(fruit1)
