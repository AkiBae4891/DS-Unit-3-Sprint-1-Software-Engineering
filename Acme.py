import random

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        if self.price/self.weight < 0.5:
            return "Not so stealable..."
        elif self.price/self.weight >= 0.5 and self.price/self.weight < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        if self.flammability * self.weight < 10:
            return "...fizzle."
        elif self.flammability * self.weight >= 10 and self.flammability * self.weight < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

    def __repr__(self):
        return self.name

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        if self.flammability * self.weight:
            return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "Ouch!"
