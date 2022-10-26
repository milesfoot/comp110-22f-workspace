"""Dictionary Functions."""


__author__: str = "730613797"


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the values and keys within a list."""
    new_dict = {}
    for value in old_dict:
        if value not in new_dict:
            new_dict = dict([value, key] for key, value in old_dict.items())
        else:
            raise KeyError("Duplicate Keys, Turn Back!")
    return new_dict
    

def favorite_color(colors: dict[str, str]) -> str:
    """Determines the color most frequently inputed as a value."""
    color_count = {}
    for key, value in colors.items():
        if value not in color_count:
            color_count[value] = 0
        else:
            color_count[value] += 1     
    return((max(color_count, key = color_count.get)))


def count(items: list[str]) -> dict[str, int]:
    """Counting the frequency of a certain value!"""
    new_dict = {}
    sett = set()
    for i in items:
        if i in sett:
            new_dict[i] = new_dict[i] + 1
        else:
            new_dict[i] = 1
            sett.add(i)
    return new_dict