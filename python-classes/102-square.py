#!/usr/bin/python3
class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): The size of each side of the square (private).

    Methods:
        __init__(self, size=0): Initializes a new Square object with the given size.
        area(self): Calculates and returns the current square area.

    """
    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (float or int, optional): The size of each side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            float or int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            float or int: The area of the square.

        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Compare if the area of this square is less than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a smaller area; otherwise, False.

        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compare if the area of this square is less than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a smaller or equal area; otherwise, False.

        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Compare if the area of this square is equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has an equal area; otherwise, False.

        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compare if the area of this square is not equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square does not have an equal area; otherwise, False.

        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compare if the area of this square is greater than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a larger area; otherwise, False.

        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compare if the area of this square is greater than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square has a larger or equal area; otherwise, False.

        """
        return self.area() >= other.area()

