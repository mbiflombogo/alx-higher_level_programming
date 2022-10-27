#!/usr/bin/python3
"""13.
Update the class Rectangle by adding
the public method def to_dictionary(self):
that returns the dictionary
representation of a Rectangle"""

from models import base
Base = base.Base


class Rectangle(Base):
    """I'm a descendant of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, wdth):
        """setter"""
        if type(wdth) != int:
            raise TypeError("width must be an intger")
        if wdth <= 0:
            raise ValueError("width must be > 0")
        self.__width = wdth

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, hgh):
        """setter"""
        if type(hgh) != int:
            raise TypeError("height must be an intger")
        if hgh <= 0:
            raise ValueError("height must be > 0")
        self.__height = hgh

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, ex):
        """setter"""
        if type(ex) != int:
            raise TypeError("x must be an intger")
        if ex < 0:
            raise ValueError("x must be >= 0")
        self.__x = ex

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, wy):
        """setter"""
        if type(wy) != int:
            raise TypeError("y must be an intger")
        if wy < 0:
            raise ValueError("y must be >= 0")
        self.__y = wy

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def display(self):
        """print Rectangle with #"""
        print("\n" * self.__y + "\n"
              .join(" " * self.__x + "#" * self.__width
                    for _ in range(self.__height)))

    def __str__(self):
        """informal str representation"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    def update(self, *args, **kwargs):
        """no-keyword arg"""
        if args and len(args) != 0:
            ls = [self.id, self.__width, self.__height, self.__x, self.__y]
            for i in range(len(args)):
                ls[i] = args[i]

            self.id = ls[0]
            self.__width = ls[len(ls) - 4]
            self.__height = ls[len(ls) - 3]
            self.__x = ls[len(ls) - 2]
            self.__y = ls[len(ls) - 1]
        else:
            for k, v in kwargs.items():
                if k == "height":
                    self.__height = v
                elif k == "width":
                    self.__width = v
                elif k == "x":
                    self.__x = v
                elif k == "id":
                    self.id = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """Dictionary representation"""
        ls = [("x", self.__x), ("y", self.__y),
              ("id", self.id), ("height", self.__height),
              ("width", self.__width)]
        return dict(ls)
