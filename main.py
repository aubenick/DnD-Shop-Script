from random import shuffle
from enum import Enum
from item import Item
import backend

# Rarity strings for ease of use adding items to JSON
common = "common"
uncommon = "uncommon"
rare = "rare"
veryrare = "veryrare"
legendary = "legendary"


def printItem(name, rarity, price):
    priceStr = ("$" + str(price))
    cols = [name, priceStr, rarity]

    print("{: <46} {: <10} {: <10}".format(*cols))


def generateTier(quantity, rarity):
    items = items[rarity]
    shuffle(items)

    for i in range(quantity):
        price = generatePrice(rarity)
        printItem(items.pop(), Rarities(rarity).name, price)

# Display all items in the JSON file


def listItems():
    items = backend.getItems()
    for item in items:
        print(item.toString())

# Adds new item to JSON, and sorts the list


def addNewItem(name, rarity, source="GS"):
    items = backend.getItems()
    newItem = Item(name=name, source=source, rarity=rarity)
    items.add(newItem)

    # Sort By Name
    sortedSet = sorted(items, key=lambda x: x.name)

    backend.writeItemsToJson(sortedSet)


def createShop(quantityGenerated):
    print("createShop", quantityGenerated, "\n")
    shopItems = backend.getItemsWithPrices(quantityGenerated)
    printShop(shopItems)
    print()


def main():
    # quantityGenerated = [3, 8, 5, 1, 0]
    # createShop(quantityGenerated)

    addNewItem("Prized Pet Protector", uncommon)
    addNewItem("Prized Pet Protector", rare)


if __name__ == "__main__":
    main()
