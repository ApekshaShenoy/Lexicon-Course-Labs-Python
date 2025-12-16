"""
10. Implement __contains__. Create a class where you can check "value in object" 
using __contains__.  

"""
class Books:
    def __init__(self,book):
        self.book = book

    def __contains__(self,book):
        return book in self.book
    

Book_list = ["The Magic","Atomic Habits","Ikigai","The Secet", "The Power"]
print("Python Basics" in Book_list)
print("Atomic Habits" in Book_list)
