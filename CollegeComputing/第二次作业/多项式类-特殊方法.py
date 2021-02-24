class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        ######### Begin #########
        sum=0
        length=len(self.coeff)
        for i in range(length):
            sum+=self.coeff[i]*x**(length-i-1)
        return sum
        ########## End ##########

    def __str__(self):
        ######### Begin #########
        s = ''
        length=len(self.coeff)
        for i in range(length):
            if self.coeff[i] != 0:
                s += '+%gx^%d' % (self.coeff[i],length-i-1)
        s = s.replace('+-','-')
        s = s.replace('x^0','')
        s = s.replace('1x','x')
        s = s.replace('x^1','x')
        if s[0:1] == '+':
            s=s[1:]
        if s[0:1] == '-':
            s='-' +s[1:]
        return s
        ########## End ##########

    def __repr__(self):
        ######### Begin #########
        return "Polynomial("+str(self.coeff)+")"
        ########## End ##########

    def __add__(self, other):
        gap = abs(len(self.coeff) - len(other.coeff))
        if len(self.coeff) > len(other.coeff):
            result = self.coeff[:]
            for i in range(len(other.coeff)-1, -1, -1):
                result[i+gap] = self.coeff[i+gap] + other.coeff[i]
        else:
            result = other.coeff[:]
            for i in range(len(self.coeff)-1, -1, -1):
                result[i+gap] = self.coeff[i] + other.coeff[i+gap]
        return Polynomial(result)

    def __sub__(self, other):
        gap = abs(len(self.coeff) - len(other.coeff))
        if len(self.coeff) > len(other.coeff):
            result = self.coeff[:]
            for i in range(len(other.coeff)-1, -1, -1):
                result[i+gap] = self.coeff[i+gap] - other.coeff[i]
        else:
            result = [(-1)*x for x in other.coeff]
            for i in range(len(self.coeff)-1, -1, -1):
                result[i+gap] = self.coeff[i] + result[i+gap]

        return Polynomial(result)

def print_(x):
    if type(x) == float:
        print("%.2f" % x)
    else:
        print(x)

def tPolynomial(coeff1, coeff2):
    p1 = Polynomial(coeff1)
    p2 = Polynomial(coeff2)
    print('"%s" + "%s" = "%s"' % (p1, p2, p1 + p2))
    print('"%s" - "%s" = "%s"' % (p1, p2, p1 - p2))

if __name__ == '__main__':
    tPolynomial([2, 3, 4, 5], [-2, 1, 0, 4])