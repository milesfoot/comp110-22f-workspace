"""EX01 - One Shot Wordle - Loops """

__author__ = "730613797"


SECRET: str = "python"
word: str = input("What is your 6-letter guess? ")
i: int = 0 
guess_boxes: str = ""
guess: bool = False
ii: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while len(word) != 6:
        word = input("That was not 6 letters! Try again: ")


while ii < len(SECRET) and guess == False:
    if word[i] == SECRET[ii]:
        guess = True
    else:

        ii += 1


while i < len(word):
    if word[i] == SECRET[i]:
        guess_boxes = guess_boxes + GREEN_BOX
    elif guess is False:
        guess_boxes = guess_boxes + WHITE_BOX
    if word[i] != SECRET[i] and guess is True:
        guess_boxes = guess_boxes + YELLOW_BOX
        guess == False
    i += 1


print(guess_boxes)
if word == SECRET:
        print("Woo! You got it!")
else:
        print("Not quite. Play again soon!")