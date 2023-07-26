#!/usr/bin/python3
import math

class MagicClass:
    """
    Represents a MagicClass that calculates the area and circumference of a circle.

    Attributes:
        __radius (int or float): The radius of the circle (private).

    Methods:
        __init__(self, radius): Initializes a new MagicClass object with the given radius.
        area(self): Calculates and returns the area of the circle.
        circumference(self): Calculates and returns the circumference of the circle.

    """
    def __init__(self, radius):
        """
        Initializes a new MagicClass object.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number (int or float).

        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.

        """
        return 2 * math.pi * self.__radius

