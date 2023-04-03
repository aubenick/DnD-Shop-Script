from random import shuffle
from item import Item
import backend

# Rarity strings for ease of use adding items to JSON
common = "common"
uncommon = "uncommon"
rare = "rare"
veryrare = "veryrare"
legendary = "legendary"


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
    print("Generating Shop.")
    print("{: <46} {: <10} {: <10} {: <4}".format(
        *["Item Name", "Price (GP)", "Rarity", "Source"]) + '\n')
    shopItems = backend.getItemsWithPrices(quantityGenerated)
    # printShop(shopItems)
    for item in shopItems:
        item.printItem()
    print()


def main():

    # quantityGenerated = [2, 7, 3, 2, 0]
    # createShop(quantityGenerated)

    addNewItem("Cloudkept Armor", veryrare)


if __name__ == "__main__":
    main()
