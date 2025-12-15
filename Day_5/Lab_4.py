"""
4. Create a class that initializes from **kwargs. Write a class where attributes are 
automatically created from keyword arguments, even when di erent objects 
receive di erent arguments. 

"""
class info:
    def __init__(self ,**kwargs):
        for key , value in kwargs.items():
            setattr(self,key,value)


Person1 = info(name = "Apeksha",age = 32)
Person2 = info(name = "Srinivas", gender = "male" ,age =38)
Person3 = info(name ="Mishika")

print(Person1.__dict__)
print(Person2.__dict__)
print(Person3.__dict__)