"""
Prac 09 - UnreliableCar class
"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """Represent an Unreliable Car Object."""

    def __init__(self, name, fuel, reliability):
        """Initialise Unreliable Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if the random number is less than the car's reliability"""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
