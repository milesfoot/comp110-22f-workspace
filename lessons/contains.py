"""Example implementing a list utility function."""

#function name: contains
# We will have 2 parametersL needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Gameplan
    # 1. Start with the first index
    i: int = 0
    # 2. Loop through every index
    while i < len(haystack):
        #   2.A Test if item at index equal to needle
        if haystack[i] == needle:
        #        2.A. True Return True! We Found it!
            return True
        i += 1
    # 3. Return False
    return False
