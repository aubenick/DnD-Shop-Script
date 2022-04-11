from random import randrange, shuffle
from enum import Enum
import backend


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    VERYRARE = 3
    LEGENDARY = 4


itemMatrix = backend.getAllItems()


def generatePrice(rarity):
    if(rarity == 0):
        return randrange(20, 75, 5)
    elif(rarity == 1):
        return randrange(100, 705, 5)
    elif(rarity == 2):
        return (randrange(1, 11) + randrange(1, 11)) * 1000
    elif(rarity == 3):
        return randrange(20000, 50500, 500)
    elif (rarity == 4):
        return randrange(1, 7) * randrange(1, 7) * 25000
    else:
        return -1


def printItem(name, rarity, price):
    priceStr = ("$" + str(price))
    cols = [name, priceStr, rarity]

    print("{: <40} {: <10} {: <10}".format(*cols))


def generateTier(quantity, rarity):
    items = itemMatrix[rarity]
    shuffle(items)

    for i in range(quantity):
        price = generatePrice(rarity)
        printItem(items.pop(), Rarity(rarity).name, price)


def createShop(quantityGenerated):
    print("createShop", quantityGenerated, "\n")
    for i in range(len(quantityGenerated)):
        generateTier(quantityGenerated[i], i)
    print()


def main():
    quantityGenerated = [3, 3, 2, 1, 1]
    createShop(quantityGenerated)


if __name__ == "__main__":
    main()
