"""
6. Loop – Power Calculation
Write a program that takes two integers as input (base and exponent) and calculates the
power using loops.
"""

def power(a,b):
  result = 1
  
  for _ in range(b):
    result *= a
    print(result)
  return result

int1 = int(input("Enter integer1: "))
int2 = int(input("Enter integer2: "))
print("Calculating {} to the {} using loops results in :".format(int1,int2),power(int1,int2))
