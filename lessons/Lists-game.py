"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# remove item from list by index
rolls.pop(len(rolls) - 1)
print(rolls) 
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # access an individual
# print(rolls[0])
# print(rolls[1])

# #access the length of a list
# print(len(rolls))

# #access the last item of list
# list_index: int = len(rolls) - 1 
# # either or
# print(rolls[len(rolls) - 1])


