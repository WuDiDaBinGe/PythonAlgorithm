from math import pi,sqrt
class Shape(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.draw()
    def area(self):
        # 需要在子类中重写
        pass

    def perimeter(self):
        # 需要在子类中重写
        pass

    def draw(self):
        # 需要在子类中重写
        pass

    def __str__(self):
        return "Area is :%.2f, Perimeter is :%.2f" % (self.area(), self.perimeter())

class Circle(Shape):
    ############Begin##################


    ############End####################



class RightTriangle(Shape):
    ############Begin##################


    ############End####################


class Rectangle(Shape):
    ############Begin##################



    ############End####################



class ShapeFactory(object):

    ############Begin##################

    @staticmethod
    def getShape(classname, a, h):


    ############End####################



def simple_factory_test():
    c = ShapeFactory.getShape("Circle", 3, 3)
    print(c)
    b = ShapeFactory.getShape("Rectangle", 100, 600)
    print(b)
    s = ShapeFactory.getShape("RightTriangle", 3, 4)
    print(s)


if __name__ == '__main__':
    simple_factory_test()