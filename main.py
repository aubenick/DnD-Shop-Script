from random import shuffle
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


def listItems():
    # Function: Display all items in the JSON file
    items = backend.getItems()
    for item in items:
        print(item.toString())


def addNewItem(name, rarity, source="GS"):
    # Function: Adds new item to JSON, and sorts the list.
    items = backend.getItems()
    newItem = Item(name=name, source=source, rarity=rarity)
    items.add(newItem)

    # Sort By Name
    sortedSet = sorted(items, key=lambda x: x.name)

    backend.writeItemsToJson(sortedSet)


def createShop(quantityGenerated):
    print("createShop", quantityGenerated, "\n")
    # shopItems = backend.getItemsWithPrices(quantityGenerated)
    # printShop(shopItems)
    print()


def main():
    # quantityGenerated = [3, 8, 5, 1, 0]
    # createShop(quantityGenerated)

    addNewItem("Hedgewitch's Gardening Gloves", uncommon)


if __name__ == "__main__":
    main()
