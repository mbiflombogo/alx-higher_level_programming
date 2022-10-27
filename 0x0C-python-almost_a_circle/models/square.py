#!/usr/bin/python3
"""12.
Update the class Square by adding
the public method def update
(self, *args, **kwargs) that
assigns attributes"""

import json
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """I'm a descendant of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, sz):
        """Setter"""
        if type(sz) != int:
            raise TypeError("width must be an intger")
        elif sz <= 0:
            raise ValueError("width must be > 0")
        self.width = sz
        self.height = sz

    def __str__(self):
        """informal str representation"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y,
                        self.width))

    def update(self, *args, **kwargs):
        """Key worded & non-keyworded args"""
        if args and len(args) != 0:
            ls = [self.id, self.size, self.x, self.y]
            for i in range(len(args)):
                ls[i] = args[i]

            self.id = ls[0]
            self.size = ls[len(ls) - 3]
            self.x = ls[len(ls) - 2]
            self.y = ls[len(ls) - 1]
        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "id":
                    self.id = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dict representation"""
        ls = [("id", self.id), ("size", self.size),
              ("x", self.x), ("y", self.y)]
        return dict(ls)
