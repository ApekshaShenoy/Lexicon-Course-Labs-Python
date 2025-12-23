class Animal:
    def __init__(self, name):
        self.name = name
        self.energy = 5
        self.is_awake = True
        self.is_angry = False

    def wake_up(self):
        self.is_awake = True
        print(f"{self.name} wakes up.")

    def eat(self):
        if self.is_awake:
            self.energy = min(5, self.energy + 1)
            print(f"{self.name} eats. Energy is now {self.energy}.")

    def play(self):
        if self.is_awake and not self.is_angry and self.energy > 1:
            self.energy -= 1
            print(f"{self.name} plays. Energy is now {self.energy}.")
        else:
            print(f"{self.name} cannot play.")

    def sleep(self):
        self.is_awake = False
        self.energy = min(5, self.energy + 2)
        print(f"{self.name} sleeps. Energy is now {self.energy}.")

    def get_angry(self):
        self.is_angry = True
        print(f"{self.name} is angry!")

class Herbivore(Animal):
    def eat(self):
        if self.is_awake:
            self.energy = min(5, self.energy + 1)
            print(f"{self.name} eats plants. Energy is now {self.energy}.")

class Carnivore(Animal):
    def eat(self):
        if self.is_awake:
            self.energy = min(5, self.energy + 2)
            print(f"{self.name} eats meat. Energy is now {self.energy}.")


