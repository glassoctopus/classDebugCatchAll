from habitats import Habitat
from movements import ISwimming

class Aquarium(Habitat):
    
    def __init__(self, name):
        super().__init__(name)
        
    def add_swimmer_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal} can\'t swim, so please don\'t try and drown the poor thing in the {self.name} habitat')

    def add_swimmer_type_check(self, animal):
        if isinstance(animal, ISwimming):
            self.animals.add(animal)
        else:
            print(f'{animal} can\'t swim, don\'t be dumb and put \'em in the {self.name}')