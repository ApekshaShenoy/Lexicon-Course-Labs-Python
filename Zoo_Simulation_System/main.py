# main simulation file

from animal import Deer, Rabbit, Lion
from visitor import Visitor
from zookeeper import ZooKeeper
import random

# creating animals
deer = Deer("Deer", 3)
rabbit = Rabbit("Rabbit", 2)
lion = Lion("Lion", 10)

# putting all animals in a list
animals = [deer, rabbit, lion]

# creating visitor and zookeeper
visitor = Visitor("Alice")
keeper = ZooKeeper("Bob")

days = 2  # number of days to run the simulation

for day in range(1, days + 1):
    print(f"\n===== Day {day} =====")

    print("\n--- Morning ---")
    # animals wake up in the morning
    for animal in animals:
        print(animal.wake_up())

    # zookeeper feeds all animals
    for message in keeper.feed_all_animals(animals):
        print(message)

    # animals play after eating
    for animal in animals:
        print(animal.play())

    # calling unique species behaviors
    print(deer.run())
    print(rabbit.play())
    print(lion.roar())

    print("\n--- Midday ---")
    # visitor may annoy animals randomly
    for animal in animals:
        if random.choice([True, False]):
            print(visitor.annoy_animal(animal))

    # zookeeper calms angry animals
    for animal in animals:
        result = keeper.calm_animal(animal)
        if result:
            print(result)

    # animals try to play again
    for animal in animals:
        print(animal.play())

    print("\n--- Evening ---")
    # feeding animals again in the evening
    for message in keeper.feed_all_animals(animals):
        print(message)

    print("\n--- Night ---")
    # animals sleep at night
    for animal in animals:
        print(animal.sleep())

    print("\n--- Daily Summary ---")
    # show final state of each animal
    for animal in animals:
        print(f"{animal.name}: energy={animal.energy}, angry={animal.is_angry}")
