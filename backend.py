common = "common.txt"
uncommon = "uncommon.txt"
rare = "rare.txt"
veryrare = "veryrare.txt"
legendary = "legendary.txt"


def getItems(fileName):
    f = open("itemLists/"+fileName, "r")
    listOfItems = []
    for item in f:
        listOfItems.append(item.rstrip('\n'))
        #f2 = open("itemLists/new" + fileName, "a")
        #f2.write(item.rstrip('\n') + " (5e)\n")
        # f2.close
    f.close()
    return listOfItems


def getAllItems():
    itemMatrix = {}
    itemFiles = [common, uncommon, rare, veryrare, legendary]

    for rarity in range(len(itemFiles)):
        itemMatrix[rarity] = getItems(itemFiles[rarity])
    return itemMatrix
