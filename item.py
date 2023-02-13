from random import randrange
import json


class Item(object):

    price = None

    # Constructor using Kwargs or A dictionary
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def setPrice(self):
        if(self.rarity == "common"):  # Common: (1d6+1)*10
            self.price = randrange(20, 75, 5)
        elif(self.rarity == "uncommon"):  # Uncommon:(1d6+1)*100
            self.price = randrange(100, 705, 5)
        elif(self.rarity == "rare"):  # Rare: (2d10)*1,000
            self.price = (randrange(1, 11) + randrange(1, 11)) * 1000
        elif(self.rarity == "veryrare"):  # Very Rare: (1d4+1)*10,000
            self.price = randrange(20000, 50500, 500)
        elif (self.rarity == "legendary"):  # Legendary: (2d6)*25,000
            self.price = randrange(1, 7) * randrange(1, 7) * 25000
        else:
            return -1

    def toString(self):
        return 'Name: {}\n\tSource: {}\n\tRarity: {}\n\tPrice: {}'.format(self.name, self.source, self.rarity, self.price)

    def toJson(self):
        return {"name": self.name, "source": self.source, "rarity": self.rarity}
