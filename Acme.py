import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self, price, weight):
        if self.price/self.weight < 0.5:
            return "Not so stealable..."
        elif self.price/self.weight >= 0.5 and self.price/self.weight < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self, flammability, weight):
        if flammability * weight < 10:
            return "...fizzle."
        elif flammability * weight >= 10 and flammability * weight < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

