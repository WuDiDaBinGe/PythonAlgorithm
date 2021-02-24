from math import sin


class G(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, x):
        return self.a*x*x + sin(self.b*x)

    def __str__(self):
        return "%.3f*(x**2)+sin(%.3f*x)"%(self.a, self.b)

for a in [1.0, 2.0]:
    for b in [0.4, 0.5]:
        for x in [1.57, 3.14]:
            g = G(a, b)
            print('%.3f' % (g(x)))
            print(g)

