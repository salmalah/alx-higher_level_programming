#!/usr/bin/python3
"""
Defines a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new instance

        Args:
            size: size of the new Squar
            x:  coordinate of the new Squar
            y: coordinate of the new Squar
            id: identity of the new Squar
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter of the Square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update Square

        Args:
            *args: attribute values.
            **kwargs: New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            b = 0
            for ar in args:
                if b == 0:
                    if ar is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = ar
                elif b == 1:
                    self.size = ar
                elif b == 2:
                    self.x = ar
                elif b == 3:
                    self.y = ar
                b += 1
        elif kwargs and len(kwargs) != 0:
            for t, n in kwargs.items():
                if t == "id":
                    if n is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = n
                elif t == "size":
                    self.size = n
                elif t == "x":
                    self.x = n
                elif t == "y":
                    self.y = n

    def __str__(self):
        """
        return [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width)

    def to_dictionary(self):
        """
        return the dictionary representation of the Square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
