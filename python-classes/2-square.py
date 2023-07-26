#!/usr/bin/python3
class Square:
    """
    Represents a square.
    Attributes:
        __size (int): The size of each side of the square (private).

    Methods:
        __init__(self, size=0): Initializes a new Square object with the given size.

    """
    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int, optional): The size of each side of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

