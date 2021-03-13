from math import pi,sqrt
class Shape(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self):
        pass

    def __str__(self):
        return "Area is :%.2f, Perimeter is :%.2f" % (self.area(), self.perimeter())

class Circle(Shape):

    def __init__(self, a, b):
        super(Circle, self).__init__(a, b)
        self.draw()

    def perimeter(self):
        return 2*pi*self.a

    def area(self):
        return pi*self.a*self.b

    def draw(self):
        print("Draw Circle!")


class RightTriangle(Shape):

    def __init__(self, a, b):
        super(RightTriangle, self).__init__(a, b)
        self.draw()

    def perimeter(self):
        return self.a + self.b + sqrt(self.a**2 + self.b**2)

    def area(self):
        return self.a * self.b / 2

    def draw(self):
        print("Draw RightTriangle!")

class Rectangle(Shape):

    def __init__(self, a, b):
        super(Rectangle, self).__init__(a, b)
        self.draw()

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def draw(self):
        print("Draw Rectangle!")


class ShapeFactory(object):

    @staticmethod
    def getShape(classname, a, b):
        return eval(classname+"({},{})".format(a, b))


def simple_factory_test():
    c = ShapeFactory.getShape("Circle", 3, 3)
    print(c)
    b = ShapeFactory.getShape("Rectangle", 100, 600)
    print(b)
    s = ShapeFactory.getShape("RightTriangle", 3, 4)
    print(s)


if __name__ == '__main__':
    simple_factory_test()