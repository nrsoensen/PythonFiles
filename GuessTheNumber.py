from random import *

answer = randint(1,11)
trial = 0
while trial < 3:
    guess = eval(input("Guess a number between 1 and 10!"))
    trial += 1
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
