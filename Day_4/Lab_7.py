"""
7. Creating Your Own Class
Write a class with at least two instance attributes and a method that prints or returns information based
on those attributes. Create at least two objects and demonstrate that they can have different values.
"""
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"My car is {self.brand} from the year{self.year}")
        

car_1 = Car("Audi",2020)
car_2 = Car("BMW",2018)

car_1.info()
car_1.info()
