# visitor interacts with animals but does not take care of them

class Visitor:
    def __init__(self, name):
        self.name = name

    def annoy_animal(self, animal):
        # visitors may annoy animals and make them angry
        message = animal.get_angry()
        return f"{self.name} annoys {animal.name}. {message}"
