from random import randrange


class Item(object):

    price = None

    # Constructor that uses Kwargs or dictionary to initialize
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    # Sets price of item randomly based on rarity
    def setPrice(self):
        if (self.rarity == "common"):  # Common: (1d6+1)*10
            self.price = randrange(20, 75, 5)
        elif (self.rarity == "uncommon"):  # Uncommon:(1d6+1)*100
            self.price = randrange(100, 705, 5)
        elif (self.rarity == "rare"):  # Rare: (2d10)*1,000
            self.price = (randrange(1, 11) + randrange(1, 11)) * 1000
        elif (self.rarity == "veryrare"):  # Very Rare: (1d4+1)*10,000
            self.price = randrange(20000, 50500, 500)
        elif (self.rarity == "legendary"):  # Legendary: (2d6)*25,000
            self.price = randrange(1, 7) * randrange(1, 7) * 25000
        else:
            return -1

    # Print item as string format
    def toString(self):
        return 'Name: {}\n\tSource: {}\n\tRarity: {}\n\tPrice: {}'.format(self.name, self.source, self.rarity, self.price)

    # Prints item in JSON export format, doesn't include price as that should be instanced individually
    def toJson(self):
        return {"name": self.name, "source": self.source, "rarity": self.rarity}

    def printItem(self):
        priceStr = ("$" + str(self.price))
        cols = [self.name, priceStr, self.rarity, self.source]

        print("{: <46} {: <10} {: <10} {: <4}".format(*cols))
