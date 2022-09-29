"""EX05 - Implementing - Utils!"""

__author__: str = "730613797"


def only_evens(ints: list[int]) -> list:
    """Returning only even numbers out of a list."""
    even_list: list = []
    for i in ints:
        if i % 2 == 0:
            even_list.append(i)
    return even_list 


def concat(one_list: list[int], two_list: list[int]) -> list:
    """Making a list comprised of the first list behind the second."""  
    both_lists: list = []
    for i in one_list:
        both_lists.append(i)
    for i in two_list:
        if len(both_lists) >= len(one_list):
            both_lists.append(i)
    return both_lists


def sub(og_list: list[int], first: int, end: int) -> list:
    """Returning a subset list within the specified indices."""
    new_list: list = []
    if first < 0:
        first: int = 0
    if first > len(og_list):
        return []
    if end > len(og_list):
        end: int = (len(og_list) + 1)
    if end <= 0:
        return [] 
    if len(og_list) == 0:
        return []
    while first < (end - 1):
        if first < end:
            new_list.append(og_list[first])
        first += 1
    return new_list