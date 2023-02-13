import json
from item import Item


# Return all items from JSON file as a set
def getItems(filePath="items.json"):
    f = open(filePath, "r")
    rawList = json.load(f)
    itemSet = {Item(item) for item in rawList}
    f.close()
    return itemSet


# Saves Items to JSON Files
def writeItemsToJson(items=getItems()):
    f = open("items.json", "w")
    # Convert Item object instances to Json Strings
    itemsDict = [item.toJson() for item in items]
    json.dump(itemsDict, f, indent=4)
