"""
Task 5: Static utility methods 
Create a class that acts as a utility container. 
The class should contain multiple static methods. 
Each static method should perform a small, independent operation. 
Demonstrate usage without creating any class instances. 

"""
class Math_Ops:

    @staticmethod
    def square(a):
        return a * a
    
    @staticmethod
    def sqrt(a):
        return a ** 0.5  
    
    @staticmethod
    def power(a, b):
        return a ** b


print(Math_Ops.square(15))  
print(Math_Ops.sqrt(225))   
print(Math_Ops.power(2, 5)) 
