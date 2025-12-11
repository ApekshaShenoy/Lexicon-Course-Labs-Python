"""
LAB 1 — Range & Loops (Numbers and Iteration) 
Create a program that: 
1. Prints all odd numbers from 1–20 
2. Calculates and prints the sum of numbers from 1–100 
3. Asks the user for a number and prints its multiplication table (1–10) 
Goal: Practice range(), loops, and numeric iteration. 
"""
# 1
for num in range(1,20): 
    if num % 2 != 0:
        print(num, end=" ")

result = 0
for num in range(1,101):
    result += num
#2
print(f"\n Sum is : {result}")

#3
my_number = int(input("Enter you number:"))
table = 1

for num in range(1,11):
    table = my_number * num
    print(table, end =" ")
     