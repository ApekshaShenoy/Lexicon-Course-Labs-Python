"""
4. Local Variable Shadowing a Global Variable
Create an example where a global variable and a local variable have the same name. The program
should demonstrate which value is used inside the function and which is used outside.
"""

post_code = 15145

def present_post():
    post_code = 15248
    print(f"Inside function : {post_code}") 

present_post() # local
print(f"Outside function : {post_code}") #global