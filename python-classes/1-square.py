#!/usr/bin/python3
class Square:
    """
    Represents a square.

    A square is a geometrical shape with four equal sides and four right angles.
    Attributes:
        __size (int): The size of each side of the square (private).

    Methods:
        __init__(self, size): Initializes a new Square object with the given size.

    """
    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of each side of the square.

        """
        self.__size = size

