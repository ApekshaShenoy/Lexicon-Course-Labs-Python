"""
14. Create a dictionary using a dict comprehension. Use two lists and combine them 
into a dictionary via comprehension.  

"""

keys = ["Name","Age","City"]
values = ["Apeksha",32,"Stockholm"]

MyDictionary = {key:value for key,value in zip(keys,values)}
print(MyDictionary)