import random
def Loot(luck):
    Treasury=["Empty Pot", "Simple Earrings", "Necklace", "Apple", "Glowing Stone", "Gypsy's Blessing", "Strange Parchment", "Grinding Stone", "Gauntlet"]
    found=random.choices(Treasury, weights=[1,2,1,5,1*luck,3//luck, 1,3,3])
    if found==Treasury[0]:
        return Treasury[0], "Nothing", 0
    elif found==Treasury[1]:
        return Treasury[1], "Health", 3
    elif found==Treasury[2]:
        return Treasury[2], "Armor", 0.5
    elif found==Treasury[3]:
        return Treasury[3], "Health", 10
    elif found==Treasury[4]:
        return Treasury[4], "Energy", 10
    elif found==Treasury[5]:
        return Treasury[5], "Luck", 0.5
    elif found==Treasury[6]:
        return Treasury[6], "Luck", 0.3
    elif found==Treasury[7]:
        return Treasury[7], "Attack", 1
    elif found==Treasury[8]:
        return Treasury[8], "Armor", 2