"""
12. Rewrite a loop using a list comprehension. Convert any loop-based list 
transformation into a single list comprehension.  

"""
Numbers = [1,2,3,4,5,6,7,8,9]
Numbers1 = [num**2 for num in Numbers if num % 2 == 0]
print(Numbers1)

