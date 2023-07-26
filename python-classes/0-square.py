#!/usr/bin/python3

class Square:
    """
    Represents a square.

    A square is a geometrical shape with four equal sides and four right angles.
    Attributes:
        side_length (float or int): The length of each side of the square.

    Methods:
        __init__(self, side_length): Initializes a new Square object.

    """
    def __init__(self, side_length=0):
        """
        Initializes a new Square object.

        Args:
            side_length (float or int): The length of each side of the square.

        """
        self.side_length = side_length

