class Animal:
    # base class for all animals

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 5        # energy level (1–5)
        self.is_awake = True   # awake or sleeping
        self.is_angry = False  # angry state

    def wake_up(self):
        self.is_awake = True
        print(f"{self.name} wakes up.")

    def eat(self):
        # default eating behavior
        if self.is_awake:
            self.energy = min(5, self.energy + 1)
            print(f"{self.name} eats. Energy is now {self.energy}.")

    def play(self):
        # can play only if awake, calm, and has energy
        if self.is_awake and not self.is_angry and self.energy > 1:
            self.energy -= 1
            print(f"{self.name} plays. Energy is now {self.energy}.")
        else:
            print(f"{self.name} cannot play.")

    def sleep(self):
        # sleep restores energy
        self.is_awake = False
        self.energy = min(5, self.energy + 2)
        print(f"{self.name} sleeps. Energy is now {self.energy}.")

    def get_angry(self):
        self.is_angry = True
        print(f"{self.name} is angry!")


class Herbivore(Animal):
    # plant-eating animals

    def eat(self):
        if self.is_awake:
            self.energy = min(5, self.energy + 1)
            print(f"{self.name} eats plants. Energy is now {self.energy}.")


class Carnivore(Animal):
    # meat-eating animals

    def eat(self):
        if self.is_awake:
            self.energy = min(5, self.energy + 2)
            print(f"{self.name} eats meat. Energy is now {self.energy}.")
