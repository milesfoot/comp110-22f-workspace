"""Dictionary related utility functions."""

__author__ = "730613797"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a table(list of dict)."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a dict[str, list[str]] with only the first _ rows of data in each column."""
    new_dict: dict[str, list[str]] = {}
    for column in column_table:
        first_values: list[str] = []
        if rows > len(column_table[column]):
            return column_table
        for i in range(rows):
            first_values.append(column_table[column][i])
        new_dict[column] = first_values
    return new_dict


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Producing a dictionary with only the columns specified."""
    new_dict: dict[str, list[str]] = {}
    for i in names:
        new_dict[i] = column_table[i]
    return new_dict


def concat(dict_one: dict[str, list[str]], dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combining two lists onto one another using the same key."""
    new_dict: dict[str, list[str]] = {}
    for i in dict_one:
        new_dict[i] = dict_one[i] 
    for column in dict_two:
        if column in new_dict:
            new_dict[column] += dict_two[column]
        else:
            new_dict[column] = dict_two[column]
    return new_dict


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
