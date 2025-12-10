"""
LAB 6 — List Builder 
Students must: 
1. Create a list with 5 mixed-type elements 
2. Use append() to add two new items 
3. Use pop() to remove an element 
4. Reverse the list 
5. Sort the list (if possible) 
6. Print the final result 
Goal: Practice list manipulation.
"""

my_list = [10, "hello", True, 4.5, "A"]

my_list.append("new1")
my_list.append(99)
my_list.pop()
my_list.reverse()

try:
    my_list.sort()
except:
    print("Cannot sort mixed list")

print(my_list)
