"""Creating Your Own Adventure!"""


from random import randint


__author__: str = "730613797"


points: int = 0
player: str = ""


def main() -> None:
    """Implementing the main function."""
    global points
    points += 1
    play: bool = True
    greet()
    while play is True:
        decide = input(f"Hello {player}, would you like the find 'the_victim' or 'the_killer' or 'end' ")
        if decide == "the_victim":
            the_victim()
        elif decide == "the_killer":
            the_killer(points)
        if decide == "end":
            end()
        

def greet() -> None:
    """Greets the player."""
    global player
    print("Hi Player, it is up to you to find who was killed and by who.")
    player = input(("What is your name, Player? "))
    
    
laugh_emoji: str = "\U0001F923"
people: list[str] = ["Bryan", "Penelope", "Demetrius", "Braxton", "Taylor", "Jake", "Devin", "David"]
weapons: list[str] = ["knife", "baseball bat", "spoon", "bowling ball", "gun", "plastic straw", "mini-fridge", "RPG"]
items: list[str] = ["closet", "cabinet", "desk"]


def end() -> int:
    """Ending off the function."""
    global points
    print(f"{player}, thanks for playing!")
    return points


def the_victim() -> None:
    """This finds the weapon used and the victim."""
    global points
    i = randint(0, 7)
    ii = randint(0, 7)
    key: bool = False
    danger: bool = False
    victim: str = people[i]
    item = randint(0, 2)
    killer: str = people[ii]
    decide: str = ""
    print(f"Hello {player}, your goal in this quest is too find out who was killed!")
    print("~~~Enters Room~~~")
    while key is False and danger is False:
        locked: str = input(f"This {items[item]} wont open, Do you have a key? Y/N ")
        if locked == "yes" or "Yes" or "Y":
            key is True
        while locked == "N" or "No" and danger is False:
            print(f"~~~You walk into another room and look behind the {items[randint(0, 2)]}~~~")
            print(f"You found a {weapons[randint(0, 7)]}")
            print("'It looks dangerous' you think, 'This must be the murder weapon'")
            decide = input("Can this break the lock? Yes/No ")
            if decide == "Yes" or "yes" or "Y":
                locked: str = input(f"This {items[item]} wont open, Will the weapon break it? Y/N ")
                danger = True
            elif decide == "no" or "No" or "N":
                print("Hopefully you find who it is!" + laugh_emoji)
                danger = False
            points += 1
    if key is True:
        print("~~~Clue Found~~~")
        print(f"You found the head of {victim} and the first letter of the killer's name {killer[0]}.")
        print("Continue on to find the killer " + player + "!")
    points += 1


def contains_char(single: str, statement: str) -> bool: 
    """Search for a single character inside of another string of any length."""
    assert len(single) == 1
    i: int = 0
    while i < len(statement):
        if single == statement[i]:
            return True
        i += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Assigning right colored emojis for the proper letter."""
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
    """Finding if the guess is a certain length."""
    guess: str = input("Enter a " + str(length) + " character name(First letter capital): ")
    while len(guess) != length:
        guess = input("That wasn't " + str(length) + " chars! Try again: ")
    return guess


def the_killer(input: int) -> int:
    """Finding the killer by using the first letter."""
    points: int = 0
    i: int = 0
    ii = randint(0, 7)
    killer = people[ii]
    print(f"You must find the killer {player} Good Luck!")
    print("~~~Walks into the police station~~~")
    print("You see a sketch of the killer, You are gonna have to find their name!")
    print("~~~Accessing Database~~~")
    print("To find the rest of the killer's name, you have six tries.(Use your hint)")
    i: int = 1
    secret = killer
    win: bool = True
    while i <= 6 and win is True:
        print("=== Turn " + str(i) + "/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print("You guessed the killer!!!")
            win = False
        else:
            i += 1
        points += 1
    return points


if __name__ == "__main__":
    main()