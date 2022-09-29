"""EX04 - Utilization - Utils!"""

__author__ = "730613797"


def all(int_list: list[int], single: int) -> bool:
    """Determining whether a list constains only one integer."""
    if len(int_list) == 0:
        return False
    i: int = 0
    while i < len(int_list):
        if single == int_list[i]:
            i += 1
        else:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Finding the maximum integer within a function."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest: int = 0
    while i < len(int_list):
        if int_list[i] > largest:
            largest = int_list[i]
        i += 1
    return largest


def is_equal(first: list[int], second: list[int]) -> bool:
    """Searching for a certain list inside of another."""
    i: int = 0
    ii: int = 1
    if len(first) > len(second):
        return False
    if first == second:
        return True
    while i <= len(second) - len(first):
        if second[i] == first[ii]:
            check: bool = True
            i += 1
        while (i + ii) < len(second) and ii < len(first):
            if second[i + ii] != first[ii]:
                check = False
        ii += 1
        if check is True:
            return True
        i += 1
    return False        