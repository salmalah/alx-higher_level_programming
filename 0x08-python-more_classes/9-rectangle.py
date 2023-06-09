#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
Attributes:
    __width: The width of the rectangle
    __heigh: The height of the rectangle
    number_of_instances: public attribute
    print_symbol: public attribute class
Methodes:
    __init__: Initializes a new instance oif the rectangle
"""


class Rectangle:
    """
    Defines Rectangle class
    """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width: Defaults to 0.
            height: Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Returns:
            the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width

        Args:
            value: integer value of the width of the rectangle

        Raises:
            TypeError: if is not an integer
            ValueError: if the width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height

        Return:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle

        Args:
            value: integer

        Raises:
            TypeError: If is not an integer.
            ValueError: If the height < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __del__(self):
        """
        Method dletes the instance of the rectangle and print message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """
        Public instance method returns the rectangle area
        """
        return self.__width * self.__height

    def __repr__(self):
        """
        methode  recreate a new instance by using eval()
        Return:
            a string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        method that returns the biggest rectangle based on the area
        Raises:
        TypeError: If either rect_1 or rect_2 is not an instance of Rectangle
        Return:
           rectangle with the bigger area
        """
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def perimeter(self):
        """
        Method  returns the rectangle perimete
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @classmethod
    def square(cls, size=0):
        """
        method Creates a new Rectangle instance with equal width and height
        Arg:
           size: defult 0
        """
        return cls(size, size)

    def __str__(self):
        """
        methode  print the rectangle with the character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        sym = str(self.print_symbol)
        return "\n".join([sym * self.__width] * self.__height)
