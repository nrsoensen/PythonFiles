import sys

list = []
mostCommon = {}

allBreeds = ["Singapura","Oriental","LaPerm","Munchkin","Bambino","Exotic Shorthair","Persian","Abyssinian","Sphynx","Siamese","Scottish Fold","Cornish Rex",
"Devon Rex","Birman","Burmese","Tonkinese","Russian Blue","Egyptian Mau","Manx","Japanese Bobtail","Selkirk Rex","American Curl","Somali","Turkish Angora",
"Colorpoint Shorthair","Balinese","Ragamuffin","European Burmese","Bombay","Havana Brown","American Bobtail","Burmilla","Korat","Bengal","Cymric","Himalayan",
"Munchkin","Nebelung","Savannah","Snowshoe","Toyger","Aegean","Australian Mist","American Polydactyl","Arabian Mau","Malayan","Asian Semi-longhair",
"Brazilian Shorthair","Chantilly-Tiffany","Chausie","Javanese","British Shorthair","American Shorthair","Norwegian Forest Cat","Ocicat","Selkirk Rex","Chartreux",
"Ragamuffin","American Bobtail","Turkish Van","American Wirehair","Himalayan","Pixie-bob","Savannah","British Semi-longhair","Cheetoh","Cyprus","Maine Coon",
"Ragdoll","Siberian","California Spangled","Pixie-bob"]

#sizes
smallest = ["Singapura"]

small = ["Oriental","LaPerm","Munchkin","Bambino"]

medium = ["Exotic Shorthair","Persian","Abyssinian","Sphynx","Siamese","Scottish Fold","Cornish Rex","Devon Rex","Birman","Burmese","Tonkinese","Russian Blue",
"Egyptian Mau","Manx","Japanese Bobtail","Selkirk Rex","American Curl","Somali","Turkish Angora","Colorpoint Shorthair","Balinese","Ragamuffin","European Burmese",
"Bombay","Havana Brown","American Bobtail","Burmilla","Korat","Bengal","Cymric","Himalayan","Munchkin","Nebelung","Savannah","Snowshoe","Toyger","Aegean",
"Australian Mist","American Polydactyl","Arabian Mau","Malayan","Asian Semi-longhair","Brazilian Shorthair","Chantilly-Tiffany","Chausie","Javanese"]

large = ["British Shorthair","American Shorthair","Norwegian Forest Cat","Ocicat","Selkirk Rex","Chartreux","Ragamuffin","American Bobtail","Turkish Van",
"American Wirehair","Himalayan","Pixie-bob","Savannah","British Semi-longhair","Cheetoh","Cyprus"]

largest = ["Maine Coon","Ragdoll","Siberian","California Spangled","Pixie-bob"]

#hair
hairless = ["Sphynx","Bambino"]

shortHair = ["Exotic Shorthair","British Shorthair","American Shorthair","Abyssinian","Siamese","Scottish Fold","Cornish Rex","Devon Rex","Oriental","Burmese",
"Tonkinese","Russian Blue","Egyptian Mau","Ocicat","Singapura","Japanese Bobtail","Selkirk Rex","Chartreux","Colorpoint Shorthair","European Burmese"]

mediumHair = ["Manx","Turkish Van","American Wirehair","Bengal","British Semi-longhair","Cyprus","Javanese"]

longHair = ["Persian","Maine Coon","Ragdoll","Scottish Fold","Norwegian Forest Cat","Birman","Siberian","Selkirk Rex","American Curl","Somali","Turkish Angora",
"Balinese","Ragamuffin","American Bobtail","LaPerm","Cymric","Himalayan","Munchkin","Nebelung","York Chocolate","Asian Semi-longhair","Chantilly-Tiffany"]

#others
hypoallergenic = ["Sphynx","Siamese","Cornish Rex","Devon Rex","Oriental","Burmese","Siberian","Russian Blue","Ocicat","Colorpoint Shorthair","Balinese","Bengal",
"Javanese"]

fluffy = ["Exotic Shorthair","Persian","Maine Coon","Ragdoll","British Shorthair","Norwegian Forest Cat","Birman","Siberian","American Curl","Somali","Balinese",
"Ragamuffin","Turkish Van","Cymric","Himalayan","Asian Semi-longhair","Brazilian Shorthair"]

house = ["Exotic Shorthair","Persian","Maine Coon","Ragdoll","British Shorthair","American Shorthair","Abyssinian","Sphynx","Siamese","Scottish Fold","Cornish Rex",
"Devon Rex","Oriental","Birman","Siberian","Tonkinese","Russian Blue","Egyptian Mau","Ocicat","Manx","Japanese Bobtail","American Curl","Chartreux","Somali",
"Turkish Angora","Colorpoint Shorthair","Balinese","Havana Brown","American Bobtail","Turkish Van","LaPerm","American Wirehair","Himalayan","Munchkin","Snowshoe",
"Toyger"]

rare = ["Sphynx","Devon Rex","Japanese Bobtail","Chartreux","Korat","Nebelung","Pixie-bob","Savannah"]

exotic = ["Persian","British Shorthair","Abyssinian","Sphynx","Siamese","Scottish Fold","Cornish Rex","Devon Rex","Norwegian Forest Cat","Birman","Siberian",
"Tonkinese","Russian Blue","Egyptian Mau","Singapura","Manx","Japanese Bobtail","Chartreux","Somali","Turkish Angora"]


def criteria(list):
    print("\nThis is how many cat breeds fit your current criteria: ", len(list), "\n\nThese are the breeds: ")
    i = 0
    while i < len(list):
        print(list[i])
        i += 1
    next = input("\nWould you like to continue? ")
    while True:
        if next == "yes":
            break
        elif next == "no":
            exit = input("Are you sure? ")
            if exit == "no":
                break
            if exit == "yes":
                sys.exit()

'''
Adds items to list without adding duplicates
'''
def change(cat):
    for i in cat:
        if i not in list:
            list.append(i)

        if i in mostCommon:
            mostCommon[i] += 1
        else:
            mostCommon[i] = 1



'''
Find most common item in all lists given
'''
def mostestCommon():
    max = 0
    cat = ""
    for key in mostCommon:
        if mostCommon[key] > max:
            max = mostCommon[key]
            cat = key
    return cat



def size():
    size = input("Which size cat would you like? (Smallest (1), small (2), medium (3), large (4), largest (5), doesn't matter (6) ")
    if size == "1":
        change(smallest)
        criteria(smallest)
    elif size == "2":
        change(small)
        criteria(small)
    elif size == "3":
        change(medium)
        criteria(medium)
    elif size == "4":
        change(large)
        criteria(large)
    elif size == "5":
        change(largest)
        criteria(largest)
    else:
        change(allBreeds)
        criteria(allBreeds)


def hair():
    hair = input("Which type of hair would you like your cat to have? (Hairless (1), short (2), medium (3), long (4), doesn't matter (5) ")
    if hair == "1":
        change(hairless)
        criteria(list)
    elif hair == "2":
        change(shortHair)
        criteria(list)
    elif hair == "3":
        change(mediumHair)
        criteria(list)
    elif hair == "4":
        change(longHair)
        criteria(list)
    else:
        criteria(list)


def other():
    other = input("\nIs there anything else? (Hypoallergenic (1), fluffy (2), house (3), rare (4), exotic (5), doesn't matter (6) ")
    if other == "1":
        change(hypoallergenic)
        criteria(list)
    elif hair == "2":
        change(fluffy)
        criteria(list)
    elif hair == "3":
        change(house)
        criteria(list)
    elif hair == "4":
        change(rare)
        criteria(list)
    elif hair == "5":
        change(exotic)
        criteria(list)
    else:
        criteria(list)


start = input("\nWould you like to take a quiz to see which cat breed would suit you best? ")
if start == "yes":
    size()
    hair()
    other()
    mostestCommon()
elif start == "no":
    print("Thank you, come again!")
    sys.exit()
