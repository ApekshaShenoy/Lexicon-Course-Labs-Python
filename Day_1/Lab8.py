"""
LAB 8 — Matrix Navigation 
Create three lists and nest them to form a matrix. Example: 
[ [1,2,3], 
[4,5,6], 
[7,8,9] ] 
Students must: 
1. Print the number in row 1, column 2 
2. Print the entire second row 
3. Print the diagonal (1,5,9) 
4. Create a new list of all first-column elements using indexing 
5. Then repeat using a list comprehension 
Goal: Practice nesting + comprehensions. 
"""

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]

matrix = [row1, row2, row3]

print("Row 1, Column 2:", matrix[0][1]) 

print("Second row:", matrix[1])

diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
print("Diagonal:", diagonal)

first_column = [matrix[0][0], matrix[1][0], matrix[2][0]] #indexing
print("First column :", first_column)

first_column_comp = [row[0] for row in matrix] #list comprehension
print("First column (list comprehension):", first_column_comp)

