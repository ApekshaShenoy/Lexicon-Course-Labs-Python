"""
LAB 3 — String Indexing & Slicing Explorer 
Given the string: 
s = "ProgrammingIsFun" 
Students must extract: 
1. The first letter 
2. The last 3 letters 
3. Every second letter 
4. The word "Programming" 
5. The word "Fun" without using indices directly (must use slicing)
6. The string reversed 
Goal: Practice indexing, slicing, stepping. 
"""
s = "ProgrammingIsFun"

print("First letter:", s[0])
print("Last 3 letters:", s[-3:])
print("Every second letter:", s[::2])
print("Programming:", s[:-5])
print("Fun:", s[-3:])
print("Reversed:", s[::-1])

