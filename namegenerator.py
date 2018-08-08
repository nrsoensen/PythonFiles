from random import *

aList = ["Ancient ","Cowardly ","Dusty ","Emerald ","Mighty ","Enchanted ","Majestic ","Salty ","Greedy ","Orange ","Chunky ","Lonely" ,"Ugliest ","Selfish ","Frightening "]
bList = ["Lion","Clover","Maid","Blade","Club","Foot","Squirrel","Quartz","Cave","Bush","Hose","Volcano","Knight","Crown","Kettle"]

aRandomIndex = randint(0, len(aList)-1)
bRandomIndex = randint(0, len(bList)-1)

print("\n\n" + "The " + aList[aRandomIndex] + bList[bRandomIndex] + "\n\n")
