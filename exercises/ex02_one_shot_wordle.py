"""EX01 - One Shot Wordle - Loops """

__author__ = "730613797"


SECRET: str = "python"
word: str = input("What is your 6-letter guess? ")
i: int = 0 
guess: bool = False
guess_boxes: str = ""
new_counter: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
while len(word) != 6:
        word = input("That was not 6 letters! Try again: ")
while i < len(SECRET):
        if word[i] == SECRET[i]: 
                guess_boxes: str = guess_boxes + GREEN_BOX
                i += 1
        else:
                guess_boxes: str = guess_boxes + WHITE_BOX
                i += 1
while new_counter < len(SECRET) and guess != False:
        if SECRET[new_counter] == word[i]:
                guess == True
                guess_boxes: str = guess_boxes + YELLOW_BOX
                new_counter += 1
        else:                       
                new_counter += 1 

print(guess_boxes)
if word == SECRET:
        print("Woo! You got it!")
else:
        print("Not quite. Play again soon!")



