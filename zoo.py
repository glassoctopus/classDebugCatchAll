from animals import Penguin, PaintedDog
from habitats import Aquarium

bob = Penguin("Bob")
ralph = PaintedDog("Ralph")

seaworld = Aquarium("Sea World")
seaworld.add_animals(bob)
seaworld.add_animals(ralph)

for animal in seaworld.animals:
    print(animal)
    

