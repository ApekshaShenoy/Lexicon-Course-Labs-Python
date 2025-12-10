"""
2. Nested List
Given the list l = [3, 7, [1, 4, 'hello']], change the value 'hello' to 'goodbye'.

"""
nest_lst = [3, 7, [1, 4, 'hello']]

nest_lst[2][2] = "goodbye"

print (f"Updated list : {nest_lst}")
