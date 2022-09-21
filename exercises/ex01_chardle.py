"""EX01 - Chardle - A cute step towards Wordle. """

__author__ = "730613797"

counter: int = 0

word: str = input("Enter a 5-letter word: ")
if len: 5
else:
    print("Error: Word must contain 5 characters") 
    quit()

single: str = input("Enter a single character: ")
if len: 1
else:
    print("Error: Character must be a single character.")
    quit()
print("Searching for " + single + " in " + word)
if single == word[2]:
    print( single + " found at index 2 ")
    counter = counter + 1
if single == word[1]:
    print( single + " found at index 1 ")
    counter = counter + 1
if single == word[0]:
    print( single + " found at index 0 ")
    counter = counter + 1
if single == word[3]:
    print( single + " found at index 3 ")
    counter = counter + 1
if single == word[4]:
    print( single + " found at index 4 ")
    counter = counter + 1

if counter == 1:
    print("1 instances of " + single + " found in " + word )
else:
    print("No instances were found")