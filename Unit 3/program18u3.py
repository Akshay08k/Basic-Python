import math


class Square:
    def area(self, x):
        print("Area of a square is %2f" % (x * x))


class Circle(Square):
    def area(self, x):
        print("Area of a circle is %2f" % (math.pi * x * x))


c = Circle()

c.area(15)


c1 = Square()

c1.area(15)
