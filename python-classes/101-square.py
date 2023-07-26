#!/usr/bin/python3
class Square:
    """
    Represents a square.
    
    Attributes:
        __size (int): The size of each side of the square (private).
        __position (tuple): The position of the square when printing (private).

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new Square object with the given size and position.
        area(self): Calculates and returns the current square area.
        my_print(self): Prints the square with the character '#' and proper positioning.

    Properties:
        size (getter, setter): A property to get and set the size attribute.
        position (getter, setter): A property to get and set the position attribute.

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.

        Args:
            size (int, optional): The size of each side of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is less than 0 or position contains negative integers.

        """
        self.size = size
        self.position = position

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
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
            ValueError: If value contains negative integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(x < 0 for x in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#', properly positioned.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Converts the square to a string for printing.

        Returns:
            str: The string representation of the square.

        """
        square_str = ""
        if self.__size == 0:
            square_str += "\n"
        else:
            for _ in range(self.__position[1]):
                square_str += "\n"
            for _ in range(self.__size):
                square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str.strip()

