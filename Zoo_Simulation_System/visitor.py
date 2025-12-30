class Visitor:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        animal.eat()
        print(f"{self.name} feeds {animal.name}.")

    def annoy_animal(self, animal):
        animal.get_angry()
        print(f"{self.name} annoys {animal.name}.")
