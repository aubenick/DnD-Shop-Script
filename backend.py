import json
from random import shuffle
from item import Item
from typing import List


# Return all items from JSON file as a set
def getItems(filePath="items.json"):
    f = open(filePath, "r")
    rawList = json.load(f)
    itemSet = {Item(item) for item in rawList}
    f.close()
    return itemSet

# Return a list of items based on rarity


def getItemsWithPrices(quantityGenerated: list[int]) -> list[Item]:
    items = getItems()
    rarities = ["common", "uncommon", "rare", "veryrare", "legendary"]
    output: List[Item] = []
    for i in range(len(quantityGenerated)):
        currentRarity = rarities[i]
        amountToGenerate = quantityGenerated[i]
        itemsAtCurrentRarity = [x for x in items if x.rarity == currentRarity]
        shuffle(itemsAtCurrentRarity)
        for j in range(amountToGenerate):
            item = itemsAtCurrentRarity[j]
            item.setPrice()
            output.append(item)

    return output


# Saves Items to JSON Files
def writeItemsToJson(items=getItems()):
    f = open("items.json", "w")
    # Convert Item object instances to Json Strings
    itemsDict = [item.toJson() for item in items]
    json.dump(itemsDict, f, indent=4)
