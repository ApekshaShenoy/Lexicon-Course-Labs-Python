"""4. Sets – Unique Values
Use a set to find the unique values in the list:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
"""
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
myset = set()

for i in mylist:
    myset.add(i)

print(myset)
