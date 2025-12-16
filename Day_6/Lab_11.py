"""
11. Implement __getitem__. Create a class that allows indexing with square brackets 
to access internal data.  

"""
class Liabrary:
    def __init__(self,book):
       self.book = book

    def __getitem__(self,index):
        return self.book[index]
    
library = Liabrary(["Python", "Java", "C++"])
print(library[1])   
