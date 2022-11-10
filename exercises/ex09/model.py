"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730613797"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> int:
        """Determining the distance between two Points."""
        distance_form: int = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance_form


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Ticks the Cell."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1 
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "yellow"
        if self.is_immune():
            return "blue"

    def contract_disease(self) -> None:
        """Makes the Cell now infected."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Determines if the cell is vulnerable based off of its infection status."""
        if self.sickness == constants.VULNERABLE:
            return True
        else: 
            return False

    def is_infected(self) -> bool:
        """Determines if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True    
        if self.sickness == constants.INFECTED:
            return True
        else: 
            return False

    def contact_with(self, other: Cell) -> None:
        """Determines if the cell is in contact with another."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()

    def immunize(self) -> None:
        """Makes the cell immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Checking the cell to be immune and returning T/F."""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_cells <= 0 or infected_cells >= cells:
            raise ValueError("Some # of Cell objects must begin infected")
        if immune_cells >= cells:
            raise ValueError("Check # of Immune Cells")
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(infected_cells):
            self.population[i].contract_disease()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
    
    def check_contacts(self) -> None:
        """Checking when two points make contact."""
        ii: int = 1
        for i in range(len(self.population)):
            for j in range(len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                ii += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True
