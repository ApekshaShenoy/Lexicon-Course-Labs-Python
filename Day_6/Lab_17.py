"""
17. Demonstrate LEGB with nested functions. Create a function that contains 
another function. Use variables with the same name at multiple levels and 
demonstrate which is used where. Modify the enclosing variable using nonlocal.  

"""
identity = "Indian Passport"

def enter_sweden():
    identity = "Residence Permit"

    def in_swdeden():
        nonlocal identity
        identity = "Swedish National Id"
        print(f"When in Sweden I use :{identity}")

    in_swdeden()
    print(f"When we enter Sweden I use :{identity}")

enter_sweden()
print(f"Globally I use {identity} for identification")


