# zookeeper is responsible for animal care

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_all_animals(self, animals):
        # feeds every animal in the zoo
        messages = []
        for animal in animals:
            messages.append(f"{self.name} feeds {animal.name}.")
            messages.append(animal.eat())
        return messages

    def calm_animal(self, animal):
        # calms angry animals
        if animal.is_angry:
            animal.is_angry = False
            return f"{self.name} calms {animal.name}."
        return None
