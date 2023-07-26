#!/usr/bin/python3
class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of each side of the square (private).

    Methods:
        __init__(self, size=0): Initializes a new Square object with the given size.
        area(self): Calculates and returns the current square area.

    Properties:
        size (getter, setter): A property to get and set the size attribute.

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
        self.size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

