"""EX03 - Structured Wordle - Words"""

__author__: str = "730613797"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(single: str, statement: str) -> bool: 
    #"""Search for a single character inside of another string of any length. """
    assert len(single) == 1
    i: int = 0
    while i < len(statement):
        if single == statement[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    i: int = 0
    guess_box: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            guess_box = guess_box + GREEN_BOX
        if guess[i] != secret[i] and contains_char(guess[i], secret) is True:
            guess_box = guess_box + YELLOW_BOX
        if contains_char(guess[i], secret) is False:
            guess_box = guess_box + WHITE_BOX
        i += 1
    return guess_box


def input_guess(length: int) -> str:
    guess: str = input("Enter a " + str(length) + " character word: ")
    while len(guess) != length:
        guess = input("That wasn't " + str(length) + " chars! Try again: ")
    return guess


def main() -> None:
    #"""The entrypoint of the main loop of the program"""
    i: int = 1
    secret: str ="codes"
    win: bool = True
    while i <= 6 and win == True:
        print("=== Turn " + str(i) + "/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print("You won in " + str(i) + "/6 turns!")
            win = False
        else:
            i += 1
        if i > 6:
            print("X/6 - Sorry, try again tomorrow")


if __name__ == "__main__":
    main()
