"""
19. Create a class that builds itself from a dictionary. Write a class that receives a 
dictionary and turns every key/value pair into attributes. Build __str__ using a 
comprehension.

"""
class DictObject:
    def __init__(self,data):
        for key,value in data.items():
            setattr(self,key,value)

    def __str__(self):
        return "\n".join(f"{key}={value}" for key,value in self.__dict__.items())
    
data = {"name": "Apeksha", "age": 32, "city": "Stockholm"}
obj = DictObject(data)
print(obj)
