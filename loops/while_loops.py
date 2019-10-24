import random

highest = 25
answer = random.randint(1, highest)
numGuesses = 1
maxGuesses = 8

print("Guess a number between 1 and {}. You have {} guesses: ".format(
    highest, maxGuesses))

while numGuesses <= maxGuesses:
    guess = int(input())
    if guess != answer:
        if guess not in range(1, highest):
            print("Enter a number in the given range! {} guesses remaining. Try again: ".format(
                maxGuesses-numGuesses))
            numGuesses += 1
        elif guess < answer:
            print("Wrong! {} guesses remaining. Please guess higher: ".format(
                maxGuesses-numGuesses))
            numGuesses += 1
        else:
            print("Wrong! {} guesses remaining. Please guess lower: ".format(
                maxGuesses-numGuesses))
            numGuesses += 1
    else:
        if numGuesses == 1:
            print("Wow! You got it first time!")
        else:
            numGuesses += 1
            print("Congratulations! You got the number in {} guesses!".format(numGuesses))

print("Better luck next time!")
