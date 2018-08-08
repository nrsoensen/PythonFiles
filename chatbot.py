import time
from random import *
import sys

def intro():
    print("\n" + "Hello, I am a chatbot... Say something... if you want to...")
    print("Type 'help' to see my functions.")

def process_input(answer):
    if "hello " in answer or "hey " in answer or "hi " in answer:
        print("'Sup")
    elif answer == "help":
        help()
    elif answer == "joke":
        knockknock()
    elif answer == "rps":
        rps()
    elif answer == "gtn":
        gtn(answer)
    elif answer == "menu":
        menu()
    elif answer == "hangman":
        hangman()
    elif answer == "quit":
        sys.exit()
    else:
        print("Interesting...")

def help():
    print("\n" + "joke" + "\n" + "rock, paper, scissors (rps)" + "\n" +
        "guess the number (gtn)" + "\n" + "menu" + "\n" + "hangman" + "\n" + "quit" + "\n")

def hangman():
    guesses = []
    maxfails = 6
    progress = ""
    letters = 0
    list = ["utopian","dragon","dinosaur","worship","boring","muscle","polite","quartz","confused","rainstorm","zebra"]
    randlist = randint(0, len(list)-1)
    #start of loop
    def oneplayer(guesses, maxfails, progress, letters, list, randlist):
    	print("Let's begin!")
    	word = list[randlist]
    	for i in range(len(list[randlist])):
    		progress += "_"
    	while maxfails > -1:
    		if maxfails == 0:
    			print("Game over! You lose!")
    			time.sleep(0.5)
    			print("The word was: " + list[randlist] + "\n")
    			break
    		print(progress)
    		print(guesses)
    		print("You have ", + maxfails, 'lives left!')
    		time.sleep(0.5)
    		guess = input("Guess a letter: ")
    		print("\n")
    		if guess in guesses:
    			print("You've already guessed that letter!")
    			hangman_graphic(maxfails)
    			time.sleep(0.5)
    		else:
    			guesses.append(guess)
    			index = word.find(guess)
    			if index == -1:
    				maxfails -= 1
    				print("Wrong!")
    				hangman_graphic(maxfails)
    				time.sleep(0.5)
    			else:
    				while index != -1:
    					progress = progress[:index] + guess + progress[index+1:]
    					word = word[:index] + "." + word[index+1:]
    					letters += 1
    					index = word.find(guess)
    		if letters == len(list[randlist]):
                #print(progress)
    		    print("Congratulations! You win!" + "\n")
    		    break
    def twoplayer(guesses, maxfails, progress, letters):
    	word = input("Type a word for someone to guess: ")
    	word = word.lower()
    	if(word.isalpha() == False):
    		print("That's not a word!")
    	for i in range(len(word)):
    		progress += "_"
    	while maxfails > -1:
    		if maxfails == 0:
    			print("Game over! You lose!")
    			time.sleep(0.5)
    			print("The word was: " + word + "\n")
    			break
    		print(progress)
    		print(guesses)
    		print("You have ", + maxfails, 'lives left!')
    		time.sleep(0.5)
    		guess = input("Guess a letter: ")
    		print("\n")
    		if guess in guesses:
    			print("You've already guessed that letter!")
    			hangman_graphic(maxfails)
    			time.sleep(0.5)
    		else:
    			guesses.append(guess)
    			index = word.find(guess)
    			if index == -1:
    				maxfails -= 1
    				print("Wrong!")
    				hangman_graphic(maxfails)
    				time.sleep(0.5)
    			else:
    				while index != -1:
    					progress = progress[:index] + guess + progress[index+1:]
    					word = word[:index] + "." + word[index+1:]
    					letters += 1
    					index = word.find(guess)
    		if letters == len(word):
    			print(progress)
    			print("Congratulations! You win!" + "\n")
    			break
    #picture
    def hangman_graphic(maxfails):
        if maxfails == 6:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif maxfails == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif maxfails == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif maxfails == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif maxfails == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif maxfails == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
    #main code
    print("Let's play hangman!")
    players = input("Are there one or two players? (Type '1' or '2') ")
    if players == "1":
    	oneplayer(guesses, maxfails, progress, letters, list, randlist)
    else:
    	twoplayer(guesses, maxfails, progress, letters)

def menu():
    #dishes
    sides = ["soup","salad","chili","toast","nachos","bacon","shrimp","rice","mac and cheese","biscuits"]
    main = ["steak","taco","tofu","seafood","lasagna","sushi","shish kebab","dumpling","pizza","curry"]
    dessert = ["fries","cake","cookie","sundae","pudding","chips","donut","crepe","parfait","muffin"]
    monster = ["eyeball ","spider ","zombie ","kraken ","pegasus ","unicorn ","chupacabra ","golem ","bloody "]
    #random dishes
    aSides = randint(0, len(sides)-1)
    bMain = randint(0, len(main)-1)
    cDessert = randint(0, len(dessert)-1)
    dMonster = randint(0, len(monster)-1)
    eMonster = randint(0, len(monster)-1)
    fMonster = randint(0, len(monster)-1)
    #restaurants
    aList = ["Ancient ","Cowardly ","Dusty ","Emerald ","Mighty ","Enchanted ","Majestic ","Salty ","Greedy ","Orange ","Chunky ","Lonely " ,"Ugliest ","Selfish ","Frightening "]
    bList = ["Lion","Clover","Maid","Blade","Club","Foot","Squirrel","Quartz","Cave","Bush","Hose","Volcano","Knight","Crown","Kettle"]
    #random restaurants
    aRandomIndex = randint(0, len(aList)-1)
    bRandomIndex = randint(0, len(bList)-1)
    print("\n\n" + "Today you are eating at The " + aList[aRandomIndex] + bList[bRandomIndex])
    print("Your menu for today includes " + monster[dMonster] + sides[aSides] + ", " + monster[eMonster] + main[bMain] + ", and " + monster[fMonster] + dessert[cDessert] + "\n\n")


def gtn(answer):
    correct = randint(1,11)
    for trial in range(3):
        answer = eval(input("Guess a number between 1 and 10!" ))
        if(trial == 3 and answer != correct):
            print("Game Over! Try again next time!")
            break
        if(answer == correct):
            print("Congratulations! You guessed the number!")
            break
        elif(answer < correct):
            print("Try again! Guess higher!")
        elif(answer > correct):
            print("Try again! Guess lower!")

def rps():
    rps = ["rock","paper","scissors"]
    aRps = randint(0, len(rps)-1)
    answer = input("Rock, paper, or scissors? ")
    print(rps[aRps])
    #answer is rock
    if answer == "rock" and aRps == 0:
        print("Tie!")
    if answer == "rock" and aRps == 1:
        print("I win!")
    if answer == "rock" and aRps == 2:
        print("You win...")
    #answer is paper
    if answer == "paper" and aRps == 0:
        print("You win...")
    if answer == "paper" and aRps == 1:
        print("Tie!")
    if answer == "paper" and aRps == 2:
        print("I win!")
    #answer is scissors
    if answer == "scissors" and aRps == 0:
        print("I win!")
    if answer == "scissors" and aRps == 1:
        print("You win...")
    if answer == "scissors" and aRps == 2:
        print("Tie!")

def knockknock():
    knockknock = ["Cow says ","A little old lady ","Etch ","Robin ","Cash ","Spell ","To ","Kanga ","Howl ","Nanna "]
    aKnock = randint(0, len(knockknock)-1)
    answer = input("Do you wanna hear a joke? ")
    if "ye" in answer or "ok" in answer or "sure" in answer:
        joke = input("Knock knock! ")
        if "there" in joke:
            variable = input(knockknock[aKnock])
            if "cow" in variable:
                print("No, a cow says 'mooooo'!")
            elif "lady" in variable:
                print("All this time, I had no idea you could yodel.")
            elif "etch" in variable:
                print("Bless, you.")
            elif "robin" in variable:
                print("Robin you, now hand over the cash.")
            elif "cash" in variable:
                print("No thanks, I'll have some peanuts.")
            elif "spell" in variable:
                print("Okay, okay: W.H.O.")
            elif "to" in variable:
                print("It's 'to whom'?")
            elif "kanga" in variable:
                print("Actually, it's kangaroo.")
            elif "howl" in variable:
                print("Howl you know unless you open the door?")
            elif "nanna" in variable:
                print("Nanna your business.")
    else:
        print("Well okay then...")

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("\n" + "(Say something) ")
        answer = answer.lower()
        process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
