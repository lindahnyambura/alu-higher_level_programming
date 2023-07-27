#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    Class that defines a rectangle.

    Attributes:
        __width (int): Width of the rectangle (private).
        __height (int): Height of the rectangle (private).
        number_of_instances (int): Count of instances of Rectangle (public class attribute).
        print_symbol (any): Symbol used for string representation (public class attribute).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with optional width and height.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for retrieving the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public method that returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Public method that returns the rectangle perimeter."""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if not self.__width or not self.__height:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints the message Bye rectangle... when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

