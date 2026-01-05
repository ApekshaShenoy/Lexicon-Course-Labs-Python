# constants for energy limits
MAX_ENERGY = 5
MIN_ENERGY = 0


class Animal:
    # base class for all animals in the zoo

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 3          # current energy level
        self.is_awake = True     # awake or sleeping
        self.is_angry = False    # emotional state

    def wake_up(self):
        # animal wakes up in the morning
        self.is_awake = True
        return f"{self.name} wakes up."

    def eat(self):
        # default eating behavior
        if not self.is_awake:
            return f"{self.name} is sleeping and cannot eat."

        # angry animals refuse food
        if self.is_angry:
            return f"{self.name} is angry and refuses to eat."

        self.energy = min(MAX_ENERGY, self.energy + 1)
        return f"{self.name} eats. Energy: {self.energy}"

    def play(self):
        # animals can play only if awake, calm, and energetic
        if not self.is_awake:
            return f"{self.name} is sleeping."

        # angry animals lose energy instead of playing
        if self.is_angry:
            self.energy = max(MIN_ENERGY, self.energy - 1)
            return f"{self.name} is angry and wastes energy. Energy: {self.energy}"

        if self.energy <= 1:
            return f"{self.name} is too tired to play."

        self.energy -= 1
        return f"{self.name} plays. Energy: {self.energy}"

    def sleep(self):
        # sleeping restores energy
        self.is_awake = False
        self.energy = min(MAX_ENERGY, self.energy + 2)
        return f"{self.name} sleeps. Energy: {self.energy}"

    def get_angry(self):
        # animal becomes angry (for example, due to visitors)
        self.is_angry = True
        return f"{self.name} gets angry."


class Herbivore(Animal):
    # base class for plant-eating animals

    def eat(self):
        if not self.is_awake:
            return f"{self.name} is sleeping."

        if self.is_angry:
            return f"{self.name} is angry and refuses plants."

        self.energy = min(MAX_ENERGY, self.energy + 1)
        return f"{self.name} eats plants. Energy: {self.energy}"


class Carnivore(Animal):
    # base class for meat-eating animals

    def eat(self):
        if not self.is_awake:
            return f"{self.name} is sleeping."

        if self.is_angry:
            return f"{self.name} is angry and refuses meat."

        self.energy = min(MAX_ENERGY, self.energy + 2)
        return f"{self.name} eats meat. Energy: {self.energy}"


class Deer(Herbivore):
    # deer are shy and like to run away

    def run(self):
        if self.energy > 1:
            self.energy -= 1
            return f"{self.name} runs away. Energy: {self.energy}"
        return f"{self.name} is too tired to run."


class Rabbit(Herbivore):
    # rabbits get tired faster when playing

    def play(self):
        if self.energy > 2 and not self.is_angry:
            self.energy -= 2
            return f"{self.name} hops around. Energy: {self.energy}"
        return f"{self.name} is too tired to hop."


class Lion(Carnivore):
    # lions express anger by roaring

    def roar(self):
        if self.is_angry:
            return f"{self.name} roars loudly!"
        return f"{self.name} is calm."
