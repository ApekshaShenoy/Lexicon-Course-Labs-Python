class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_all_animals(self, animals):
        for animal in animals:
            if animal.is_awake:
                animal.eat()
                print(f"{self.name} feeds {animal.name}.")

    def calm_animal(self, animal):
        if animal.is_angry:
            animal.is_angry = False
            print(f"{self.name} calms {animal.name}.")
