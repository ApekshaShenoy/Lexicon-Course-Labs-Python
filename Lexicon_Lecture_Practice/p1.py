# 1. Name assignment will create or change local names vy default
# 2. Name references search (at most) four scopes, these are: (LEGB rule)
    # Local- Name assigned in any way within a function (def or lambda) and not declared global in that function
    # Enclosing functions - Name in the local scope of any and all enclosing func, inner or outer
    # Global - Names assigned at the top-level of a module file, or declared globaly in a def within a file
    # Built-in - Built-in names, module, range.....(all that is built in)
# 3. Names declared in global and nonlocal statement map assigned names to enclosing module and function scopes
 
"""
#(Local) x is local:

f = lambda X : x**2

#Enclosing function

name = "This is some global name"

def greet():
    name = "Erik"

    def hello():
        print("hello "+name)
    hello()

greet()

#built in

len()


x=50

def func(x):
        print("x is ",x)
        x=2
        print("local x to :",x)

func(x)
print("x is still :", x)


name = "This is some global name"
def greet():
    name = "Erik"

    def hello():
        name = "anna"
        print("hello "+name)
    hello()

greet()



x = 50

def func():
    global x
    print("This func now using global x")
    print("Because of global x is:",x)
    x = 2
    print("Ran func(), changed global x to :",x)

print("Before calling func()",x)
func()
print("Value of x outside of func()",x)



class Sample():
    pass

x = Sample()
print(type(x))



class Dog():
    # class object atribute:
    def __init__(self,breed,name): # constructor , self is normaally used but you can use anything else. 
        self.breed = breed    # initialize object
        self.name = name


milo = Dog("Labrador","Milo")
#frank = Dog(breed ="Huskie")

#print(milo.breed ,"\n" ,frank.breed)

print(milo.breed , milo.name)

"""

class Circle:
    pi =  3.14

    # Circle get intanntiated with radius

    def __init__(self,radius = 1):
        self.radius = radius

    # Area method  calculates the area . Note the use of self!!
    def area(self):
        return self.radius * self.radius * Circle.pi
    #Method for resetting radius
    def setRadius(self , radius):
        self.radius = radius

    # Method for getting radius
    def getradius(self):
        return self.radius
    
c = Circle()
c.setRadius(2)
print("Radius is " , c.getradius())
print("Area is:", c.area())

