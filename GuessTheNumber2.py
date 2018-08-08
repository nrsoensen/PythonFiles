from random import *

answer = randint(1,11)
for trial in range(3):
    guess = eval(input("Guess a number between 1 and 10!"))
    if(trial == 3 and guess != answer):
        print("Game Over! Try again next time!")
        break
    if(guess == answer):
        print("Congratulations! You guessed the number!")
        break
    elif(guess < answer):
        print("Try again! Guess higher!")
    elif(guess > answer):
        print("Try again! Guess lower!")
