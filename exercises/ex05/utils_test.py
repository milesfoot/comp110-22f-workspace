"""Unit Test functions"""

__author__: str = "730613797"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub

def test_only_evens_empty() -> None:
    ints: list[int] = []
    assert only_evens(ints) == []


def test_only_evens_many_items() -> None:
    ints: list[int] = [1, 4, 7, 10, 13, 16, 19, 22, 25]
    assert only_evens(ints) == [4, 10, 16, 22] 

def test_only_evens_odds() -> None:
    ints: list[int] = [7, 31, 45]
    assert only_evens(ints) == []


def test_concat_empty_list() -> None:
    one_list: list[int] = []
    two_list: list[int] = [1, 5, 6]
    assert concat(one_list, two_list) == [1, 5, 6]


def test_concat_repeat() -> None:
    one_list: list[int] = [3, 3]
    two_list: list[int] = [4, 6, 3]
    assert concat(one_list, two_list) == [3, 3, 4, 6, 3]


def test_concat_alternate_length() -> None:
    one_list: list[int] = [7, 8, 9]
    two_list: list[int] = [1]
    assert concat(one_list, two_list) == [7, 8, 9, 1]


def test_sub_negative() -> None:
    og_list: list[int] = [4, 3, 2, 1]
    first: int = -2
    end: int = 4
    assert sub(og_list, first, end) == [4, 3, 2]


def test_sub_many_items() -> None:
    og_list: list[int] = [11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51]
    first: int = 2
    end: int = 11
    assert sub(og_list, first, end) == [19, 23, 27, 31, 35, 39, 43, 47]

def test_sub_limit() -> None:
    og_list: list[int] = [4, 3, 2, 1]
    first: int = 1
    end: int = 8
    assert sub(og_list, first, end) == [3, 2, 1]


