"""

LAB 2 — Variables & Reassignment 
Students must: 
1. Create variables for salary, bonus, and tax_rate. 
2. Calculate: 
o total income 
o taxes 
o net income 
3. Reassign variables to simulate a raise and recalc everything. 
Goal: Understand variable assignment and updating values. 

"""
salary = 45000
bonus = 8000
tax_rate = 0.33

total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes

print("Total income:", total_income)
print("Taxes:", taxes)
print("Net income:", net_income)

salary = 60000
bonus = 7000

total_income = salary + bonus
taxes = total_income * tax_rate
net_income = total_income - taxes

print("After raise:")
print("Total income:", total_income)
print("Taxes:", taxes)
print("Net income:", net_income)