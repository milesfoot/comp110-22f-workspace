"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730613797"


class Simpy:
    """Like NumPy, uses automagical operators and operator overload."""
    values: list[float] = []

    def __init__(self, values: list[float]):
        """Initializing the function."""
        self.values = values

    def __repr__(self) -> str:
        """Making the list into a string interpretation."""
        return f"Simpy({self.values})"
   
    def fill(self, floats: float, num_values: int) -> None:
        """Filling a list with the floats given only a __ amount of times."""
        self.values: Simpy = []
        for i in range(num_values):
            self.values.append(floats)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arranges the values within a list following the step but not exceeding stop."""
        assert step != 0.0
        self.values.append(start)
        count: int = int(stop / step)
        for i in range(count):
            if self.values[-1] == stop - step:
                return
            if i != start:
                num: float = step + (self.values[-1])
                self.values.append(num)

    def sum(self) -> float:
        """Calculating the sum of the following values."""
        total: float = 0.0
        i: int = 0
        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding the two items at a given index within two seperate lists."""
        new_simpy: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                new_simpy.values.append(self.values[i] + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                new_simpy.values.append(self.values[i] + rhs.values[i])
        return new_simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Taking the input and mulitplying it to the power of the second argument."""
        new_simpy: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                new_simpy.values.append(self.values[i] ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                new_simpy.values.append(self.values[i] ** rhs.values[i])
        return new_simpy

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of the times when the index of two lists or a list and float are equal."""
        new_simpy: list[bool] = []
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                new_simpy.append(self.values[i] == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                new_simpy.append(self.values[i] == rhs.values[i])
        return new_simpy

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of bools to be true if the index is greater in the first list than second."""
        new_simpy: list[bool] = []
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                new_simpy.append(self.values[i] > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                new_simpy.append(self.values[i] > rhs.values[i])
        return new_simpy

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gets the item called but can call the entire class or float."""
        new_simpy: Simpy = Simpy([])
        if isinstance(rhs, int):
            for i in range(len(self.values)):
                return self.values[rhs]
        else:
            for i in range(len(self.values)):
                if rhs[i] is True:
                    new_simpy.values.append(self.values[i])
            return new_simpy