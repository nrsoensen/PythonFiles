import time
from random import *

guesses = []
maxfails = 6
progress = ""
letters = 0
list = ["utopian","dragon","dinosaur","worship","boring","muscle","polite","quartz","confused","rainstorm","zebra","blossom","creepy"]
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
			print(progress)
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
