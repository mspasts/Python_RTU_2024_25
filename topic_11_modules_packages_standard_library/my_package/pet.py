# let's hold Pet class here

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def get_sound(self, sound):
        return f"{self.name} says {sound}"
    
# i could hold other classes here that inherit from Pet such as Dog, Cat, Fish, etc.