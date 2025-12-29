from animal import Herbivore, Carnivore
from visitor import Visitor
from zookeeper import ZooKeeper

# creating animals
deer = Herbivore("Deer", 3)
rabbit = Herbivore("Rabbit", 2)
lion = Carnivore("Lion", 10)

# keeping animals in a list to manage them easily
animals = [deer, rabbit, lion]

# creating visitor and zookeeper
visitor = Visitor("Alice")
keeper = ZooKeeper("Bob")

print("\n--- Morning ---")
# animals wake up in the morning
for animal in animals:
    animal.wake_up()

# zookeeper feeds all animals
keeper.feed_all_animals(animals)

# animals play after eating
for animal in animals:
    animal.play()

print("\n--- Midday ---")
# visitor annoys the lion
visitor.annoy_animal(lion)

# zookeeper calms the animal if it is angry
keeper.calm_animal(lion)

# animals try to play again
for animal in animals:
    animal.play()

print("\n--- Evening ---")
# feeding animals again in the evening
keeper.feed_all_animals(animals)

print("\n--- Night ---")
# animals sleep at night
for animal in animals:
    animal.sleep()
