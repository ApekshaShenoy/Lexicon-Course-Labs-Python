from animal import Herbivore, Carnivore
from visitor import Visitor
from zookeeper import ZooKeeper
import random

# creating animals
deer = Herbivore("Deer", 3)
rabbit = Herbivore("Rabbit", 2)
lion = Carnivore("Lion", 10)

# store animals in a list
animals = [deer, rabbit, lion]

# creating visitor and zookeeper
visitor = Visitor("Alice")
keeper = ZooKeeper("Bob")

print("\n--- Morning ---")
# animals wake up
for animal in animals:
    animal.wake_up()

# zookeeper feeds animals
keeper.feed_all_animals(animals)

# animals play
for animal in animals:
    animal.play()

print("\n--- Midday ---")
# visitor annoys a random animal
for animal in animals:
    if random.choice([True, False]):
        visitor.annoy_animal(animal)

# zookeeper calms the angry animal
for animal in animals:
    keeper.calm_animal(animal)

# animals try to play again
for animal in animals:
    animal.play()

print("\n--- Evening ---")
# feeding animals again
keeper.feed_all_animals(animals)

print("\n--- Night ---")
# animals sleep
for animal in animals:
    animal.sleep()
