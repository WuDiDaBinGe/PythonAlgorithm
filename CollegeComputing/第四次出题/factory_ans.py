from math import pi,sqrt
class Shape(object):

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    def __str__(self):
        return "a is %.2f,h is %.2f \nArea is :%.2f, Perimeter is :%.2f \n" % (self.a,self.h,self.area(), self.perimeter())

class Circle(Shape):

    def __init__(self, a, h):
        super(Circle, self).__init__(a, 0)
        self.draw()

    def perimeter(self):
        return 2*pi*self.a

    def area(self):
        return pi*self.a*self.a

    def draw(self):
        print("Draw Circle!")


class RightTriangle(Shape):

    def __init__(self, a, h):
        super(RightTriangle, self).__init__(a, h)
        self.draw()

    def perimeter(self):
        return self.a + self.h + sqrt(self.a**2 + self.h**2)

    def area(self):
        return self.a * self.h / 2

    def draw(self):
        print("Draw RightTriangle!")

class Rectangle(Shape):

    def __init__(self, a, h):
        super(Rectangle, self).__init__(a, h)
        self.draw()

    def perimeter(self):
        return 2 * (self.a + self.h)

    def area(self):
        return self.a * self.h

    def draw(self):
        print("Draw Rectangle!")


class ShapeFactory(object):

    @staticmethod
    def getShape(classname, a, h):
        return eval(classname+"({},{})".format(a, h))


def simple_factory_test():
    c = ShapeFactory.getShape("Circle", 3, 0)
    print(c)
    b = ShapeFactory.getShape("Rectangle", 100, 600)
    print(b)
    s = ShapeFactory.getShape("RightTriangle", 3, 4)
    print(s)


if __name__ == '__main__':
    simple_factory_test()