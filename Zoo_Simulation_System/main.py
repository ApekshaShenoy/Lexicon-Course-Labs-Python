from animal import Herbivore, Carnivore
from visitor import Visitor
from zookeeper import ZooKeeper


deer = Herbivore("Deer")
lion = Carnivore("Lion")
visitor = Visitor("Alice")
keeper = ZooKeeper("Bob")

print("\n--- Morning ---")
keeper.feed_all_animals([deer, lion])
deer.wake_up()
deer.play()
lion.wake_up()
lion.play()


print("\n--- Midday ---")
visitor.annoy_animal(lion)  
keeper.calm_animal(lion)     
lion.play()                  
deer.play()                   

print("\n--- Evening ---")
keeper.feed_all_animals([deer, lion])
deer.eat()
lion.eat()

print("\n--- Night ---")
deer.sleep()
lion.sleep()
