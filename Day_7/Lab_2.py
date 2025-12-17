"""
2. Modifying State Through super()  
Create a base class that stores a numeric value.  
Create two subclasses that modify this value in diAerent ways inside their 
constructors.  
Use super() so that each class in the inheritance chain contributes to the final value.  
Print the final result. 

"""
class Number:
    def __init__(self,num):
        self.num = num
        print("Initial number is:",self.num)

class MultiplyBy2(Number):
    def __init__(self, num):
        super().__init__(num)
        self.num *= 2
        print("Number after multiplied by 2:",self.num)


class Square(MultiplyBy2):
    def __init__(self, num):
        super().__init__(num)
        self.num **= 2
        print("Initial number multiplied by 2 and then find its sqaure:",self.num)

number = int(input("Enter your number:"))
findsqaure = Square(number)