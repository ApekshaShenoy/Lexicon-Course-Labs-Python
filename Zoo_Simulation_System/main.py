from animal import Deer, Rabbit, Lion
from visitor import Visitor
from zookeeper import ZooKeeper
import random

# creating animals (concrete species)
deer = Deer("Deer", 3)
rabbit = Rabbit("Rabbit", 2)
lion = Lion("Lion", 10)

# putting all animals in a list
animals = [deer, rabbit, lion]

# creating visitor and zookeeper
visitor = Visitor("Alice")
keeper = ZooKeeper("Bob")

days = 2  # how many days the zoo will run

for day in range(1, days + 1):
    print(f"\n===== Day {day} =====")

    print("\n--- Morning ---")
    # animals wake up in the morning
    for animal in animals:
        animal.wake_up()

    # zookeeper feeds all animals
    keeper.feed_all_animals(animals)

    # animals play after eating
    for animal in animals:
        animal.play()

    # call unique behavior once for fun
    deer.run()       # Deer runs
    rabbit.play()    # Rabbit hops differently
    if lion.is_angry:
        lion.roar()  # Lion roars if angry

    print("\n--- Midday ---")
    # visitor may annoy animals randomly
    for animal in animals:
        if random.choice([True, False]):
            visitor.annoy_animal(animal)

    # zookeeper calms animals if needed
    for animal in animals:
        keeper.calm_animal(animal)

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

    print("\n--- Daily Summary ---")
    # showing animal states at the end of the day
    for animal in animals:
        print(f"{animal.name}: energy={animal.energy}, angry={animal.is_angry}")
