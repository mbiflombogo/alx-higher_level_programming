#!/usr/bin/python3
"""1.
write the first class Base"""

import json
import csv
import turtle


class Base:
    """I AM The Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON str representation of
        list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json str object to a file"""
        filename = cls.__name__ + ".json"
        ls = []
        if list_objs:
            for ele in list_objs:
                ls.append(cls.to_dictionary(ele))
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """Return to py object"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return instance with all attributes set"""
        if cls.__name__ == "Square":
            dmmy = cls(1)
        elif cls.__name__ == "Rectangle":
            dmmy = cls(1, 1)
        dmmy.update(**dictionary)
        return dmmy

    @classmethod
    def load_from_file(cls):
        """Return list of instances"""
        file = cls.__name__ + ".json"
        if file is None or len(file) == 0:
            return []
        t = []
        with open(file, "r", encoding="utf-8") as f:
            t = cls.from_json_string(f.read())
        for i, ele in enumerate(t):
            t[i] = cls.create(**t[i])
        return t

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize"""
        filename = cls.__name__ + ".csv"
        ls = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    ls.append(obj)
        except Exception:
            pass
        return ls

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Turtle Graphics"""
        ls = list_rectangles + list_squares
        for rects in ls:
            t = turtle.Turtle()
            t.color("red")
            t.width(2)
            t.hideturtle()
            t.penup()
            t.goto(rects.x, rects.y)
            t.showturtle()
            t.pendown()
            for j in range(2):
                t.fd(rects.width)
                t.rt(90)
                t.fd(rects.height)
                t.rt(90)
