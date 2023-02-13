import json
from item import Item


def getItems():
    f = open("items.json", "r")
    rawList = json.load(f)
    itemSet = {Item(item) for item in rawList}
    f.close()
    return itemSet


def generatePrice(rarity):
    if(rarity == "common"):  # Common: (1d6+1)*10
        return randrange(20, 75, 5)
    elif(rarity == "uncommon"):  # Uncommon:(1d6+1)*100
        return randrange(100, 705, 5)
    elif(rarity == "rare"):  # Rare: (2d10)*1,000
        return (randrange(1, 11) + randrange(1, 11)) * 1000
    elif(rarity == "veryrare"):  # Very Rare: (1d4+1)*10,000
        return randrange(20000, 50500, 500)
    elif (rarity == "legendary"):  # Legendary: (2d6)*25,000
        return randrange(1, 7) * randrange(1, 7) * 25000
    else:
        return -1


# Convert Items to JSON
def writeItemsToJson(items=getItems()):
    f = open("items.json", "w")
    # Convert Item object instances to Json Strings
    itemsDict = [item.toJson() for item in items]
    json.dump(itemsDict, f, indent=4)
