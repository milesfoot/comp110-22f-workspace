"""Dictionary function testing!"""

__author__: str = "730613797"


import pytest
from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count



def test_invert_empty() -> None:
    """Testing with an empty list."""
    old_dict: dict[str, str] = {}
    assert invert(old_dict) == {}


def test_invert_input() -> None:
    """Testing with a normal set."""
    old_dict: dict[str, str] = {'kris': 'martin', 'michael': 'jordan'}
    assert invert(old_dict) == {'martin': 'kris', 'jordan': 'michael'}


def test_invert_long() -> None:
    """Testing with a long dictionary"""
    old_dict: dict[str, str] = {'kris': 'martin', 'michael': 'jordan', 'james': 'demetrius', 'kayla': 'chase'}
    assert invert(old_dict) == {'martin': 'kris', 'jordan': 'michael', 'demetrius': 'james', 'chase': 'kayla'}


def test_favorite_color_one_color() -> None:
    colors: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_norm() -> None:
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_many() -> None:
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Marx": "purple", "Jack": "yellow", "Jacob": "purple", "Devin": "yellow", "Chelsea": "yellow", "Mercer": "blue"}
    assert favorite_color(colors) == "yellow"


def test_count_empty() -> None:
    items: list[str] = []
    assert count(items) == {}


def test_count_norm() -> None:
    items: list[str] = ["blue", "yellow", "purple", "blue", "blue"]
    assert count(items) == {'blue': 3, 'yellow': 1, 'purple': 1}


def test_count_many() -> None:
    items: list[str] = ["blue", "yellow", "yellow", "blue", "purple", "purple", "purple", "orange", "yellow", "blue", "yellow"]
    assert count(items) == {'blue': 3, 'yellow': 4, 'purple': 3, 'orange': 1}