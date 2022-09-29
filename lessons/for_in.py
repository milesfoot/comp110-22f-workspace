"""IN example of For In syntax"""

names: list[str] = ["Miles", "Kris", "Marc", "Hong"]

# example of iterating through names using a while loops
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for...in loop is the same as while loop
for name in names: 
    print(name)