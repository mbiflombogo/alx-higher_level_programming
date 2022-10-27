"""main -
testing class Base"""
b1 = Base()
print(b1.id)

b2 = Base()
print(b2.id)

b3 = Base()
print(b3.id)

b4 = Base(12)
print(b4.id)

b5 = Base()
print(b5.id)

# end of test and task 1

"""main-
testing class Rectangle"""
r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)

# end of test and task 2

"""main -
testing updated class Rectangle"""
try:
    Rectangle(10, "2")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(10, 2)
    r.width = -10
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(10, 2)
    r.x = {}
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    Rectangle(10, 2, 3, -1)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# end of test and task 3

"""main -
testing area() of
instance Rectangle"""
r1 = Rectangle(3, 2)
print(r1.area())

r2 = Rectangle(2, 10)
print(r2.area())

r3 = Rectangle(8, 7, 0, 0, 12)
print(r3.area())

# end of testing and task 4

"""main -
testing display() of
instance Rectangle"""
r1 = Rectangle(4, 6)
r1.display()

print("---")

r1 = Rectangle(2, 2)
r1.display()

# end of testing and task 5

"""main -
testing __str__ of
class Rectangle"""
r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)

r2 = Rectangle(5, 5, 1)
print(r2)

# end of testing and task 6

"""main -
testing updated display()"""
r1 = Rectangle(2, 3, 2, 2)
r1.display()

print("---")

r2 = Rectangle(3, 2, 1, 0)
r2.display()

# end of testing and task 7

"""main -
testing new function:
update()"""
r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(89)
print(r1)

r1.update(89, 2)
print(r1)

r1.update(89, 2, 3)
print(r1)

r1.update(89, 2, 3, 4)
print(r1)

r1.update(89, 2, 3, 4, 5)
print(r1)

# end of test and task 8

"""main -
testing **kwargs"""
r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(height=1)
print(r1)

r1.update(width=1, x=2)
print(r1)

r1.update(y=1, width=2, x=3, id=89)
print(r1)

r1.update(x=1, height=2, y=3, width=4)
print(r1)

# end of tests and task 9

"""main -
testing dict representation"""

r1 = Rectangle(10, 2, 1, 9)
print(r1)
r1_dictionary = r1.to_dictionary()
print(r1_dictionary)
print(type(r1_dictionary))

r2 = Rectangle(1, 1)
print(r2)
r2.update(**r1_dictionary)
print(r2)
print(r1 == r2)

# end of test and task 13

"""main -
testing class Square"""

s1 = Square(5)
print(s1)
print(s1.area())
s1.display()

print("---")

s2 = Square(2, 2)
print(s2)
print(s2.area())
s2.display()

print("---")

s3 = Square(3, 1, 3)
print(s3)
print(s3.area())
s3.display()

# end of test and task 10

"""main -
testing size setter"""

s1 = Square(5)
print(s1)
print(s1.size)
s1.size = 10
print(s1)

try:
    s1.size = "9"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# end of test and task 11

"""main -
testing *args and **kwargs"""

s1 = Square(5)
print(s1)

s1.update(10)
print(s1)

s1.update(1, 2)
print(s1)

s1.update(1, 2, 3)
print(s1)

s1.update(1, 2, 3, 4)
print(s1)

s1.update(x=12)
print(s1)

s1.update(size=7, y=1)
print(s1)

s1.update(size=7, id=89, y=1)
print(s1)

# end of test and task 12

"""main -
testing Square's to_dictionary()"""

s1 = Square(10, 2, 1)
print(s1)
s1_dictionary = s1.to_dictionary()
print(s1_dictionary)
print(type(s1_dictionary))

s2 = Square(1, 1)
print(s2)
s2.update(**s1_dictionary)
print(s2)
print(s1 == s2)

# end of test 14

"""main -
testing json_to_str"""

r1 = Rectangle(10, 7, 2, 8)
dictionary = r1.to_dictionary()
json_dictionary = Base.to_json_string([dictionary])
print(dictionary)
print(type(dictionary))
print(json_dictionary)
print(type(json_dictionary))

# end of test 15

"""main -
testing save_to_file()"""

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
Rectangle.save_to_file([r1, r2])

with open("Rectangle.json", "r") as file:
    print(file.read())

# end of test 16

"""main -
testing from_json_strign()"""

list_input = [
    {'id': 89, 'width': 10, 'height': 4},
    {'id': 7, 'width': 1, 'height': 7}
]
json_list_input = Rectangle.to_json_string(list_input)
list_output = Rectangle.from_json_string(json_list_input)
print("[{}] {}".format(type(list_input), list_input))
print("[{}] {}".format(type(json_list_input), json_list_input))
print("[{}] {}".format(type(list_output), list_output))

# end of test 17

"""main -
testing create()"""

r1 = Rectangle(3, 5, 1)
r1_dictionary = r1.to_dictionary()
r2 = Rectangle.create(**r1_dictionary)
print(r1)
print(r2)
print(r1 is r2)
print(r1 == r2)

# end of test 18

"""main -
testing load_from json"""

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file()

for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))

print("---")
print("---")

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file(list_squares_input)

list_squares_output = Square.load_from_file()

for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
    print("[{}] {}".format(id(square), square))

# end of test 19

"""main -
test 20"""

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file_csv(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file_csv()

for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))

print("---")

for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))

print("---")
print("---")

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file_csv(list_squares_input)

list_squares_output = Square.load_from_file_csv()

for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
    print("[{}] {}".format(id(square), square))

# end of test 20

""" main -
testing turtle graphics"""

list_rectangles = [Rectangle(100, 40),
                   Rectangle(90, 110, 30, 10),
                   Rectangle(20, 25, 110, 80)]
list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

Base.draw(list_rectangles, list_squares)

# end of test 21 and part 1 of tasks
