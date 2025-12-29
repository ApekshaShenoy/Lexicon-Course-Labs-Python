class Animal:
    # base class for all animals

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 5        # energy level from 1 to 5
        self.is_awake = True   # whether the animal is awake
        self.is_angry = False  # whether the animal is angry

    def wake_up(self):
        # animal wakes up
        self.is_awake = True
        print(f"{self.name} wakes up.")

    def eat(self):
        # default eating behaviour
        if self.is_awake:
            self.energy = min(5, self.energy + 1)
            print(f"{self.name} eats. Energy is now {self.energy}.")

    def play(self):
        # animal can play only if awake, calm and has energy
        if self.is_awake and not self.is_angry and self.energy > 1:
            self.energy -= 1
            print(f"{self.name} plays. Energy is now {self.energy}.")
        else:
            print(f"{self.name} cannot play.")

    def sleep(self):
        # animal sleeps and gains energy
        self.is_awake = False
        self.energy = min(5, self.energy + 2)
        print(f"{self.name} sleeps. Energy is now {self.energy}.")

    def get_angry(self):
        # animal becomes angry
        self.is_angry = True
        print(f"{self.name} is angry!")


class Herbivore(Animal):
    # herbivore animal

    def eat(self):
        # herbivores eat plants
        if self.is_awake:
            self.energy = min(5, self.energy + 1)
            print(f"{self.name} eats plants. Energy is now {self.energy}.")


class Carnivore(Animal):
    # carnivore animal

    def eat(self):
        # carnivores eat meat and gain more energy
        if self.is_awake:
            self.energy = min(5, self.energy + 2)
            print(f"{self.name} eats meat. Energy is now {self.energy}.")
