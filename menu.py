from random import *

sides = ["soup","salad","chili","toast","nachos","bacon","shrimp","rice","mac and cheese","biscuits"]
main = ["steak","taco","tofu","seafood","lasagna","sushi","shish kebab","dumpling","pizza","curry"]
dessert = ["fries","cake","cookie","sundae","pudding","chips","donut","crepe","parfait","muffin"]
monster = ["eyeball ","spider ","zombie ","kraken ","pegasus ","unicorn ","chupacabra ","golem ","bloody "]

aSides = randint(0, len(sides)-1)
bMain = randint(0, len(main)-1)
cDessert = randint(0, len(dessert)-1)
dMonster = randint(0, len(monster)-1)
eMonster = randint(0, len(monster)-1)
fMonster = randint(0, len(monster)-1)

aList = ["Ancient ","Cowardly ","Dusty ","Emerald ","Mighty ","Enchanted ","Majestic ","Salty ","Greedy ","Orange ","Chunky ","Lonely " ,"Ugliest ","Selfish ","Frightening "]
bList = ["Lion","Clover","Maid","Blade","Club","Foot","Squirrel","Quartz","Cave","Bush","Hose","Volcano","Knight","Crown","Kettle"]

aRandomIndex = randint(0, len(aList)-1)
bRandomIndex = randint(0, len(bList)-1)

print("\n\n" + "Today you are eating at The " + aList[aRandomIndex] + bList[bRandomIndex])

print("Your menu for today includes " + monster[dMonster] + sides[aSides] + ", " + monster[eMonster] + main[bMain] + ", and " + monster[fMonster] + dessert[cDessert] + "\n\n")
