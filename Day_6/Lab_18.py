"""
18. Create a class that processes input using a comprehension. Write a class that 
receives a list or dictionary and transforms or filters the data internally using a 
comprehension.
"""
class DictProcessor:
    def __init__(self, data):
        self.processed = {key : value.upper() for key,value in data.items() if isinstance(value,str)}

    def __str__(self):
        return f"Processed dictionary: {self.processed}"
    
data = {"name": "Apeksha", "age": 32, "city": "Stockholm"}
dp = DictProcessor(data)
print(dp)


