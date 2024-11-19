import random

secretNum = random.randint(1, 1000)
giveUp = False
win = False

print("I have a secret number between 1 and 1000. Can you guess it?")

while (not giveUp) and (not win):
    guess = input()
    if guess == "Give Up":
        giveUp = True
        print("The secret number was", secretNum, ". You Failure!!")
    else:
        guess = int(guess)
        if guess == secretNum:
            print("You guessed the number!")
            win = True
        elif guess < secretNum:
            print("Too low, try again.")
        elif guess > secretNum:
            print("Too high, try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 1000.")