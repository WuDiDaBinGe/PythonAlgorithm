import numpy as np


class LuUtils(object):
    @staticmethod
    def LU(A):
    ############Begin#############


    ############End#############


def LUsolve(A, b):


############Begin#############


############End#############


def getSlove():
    A = np.array([[1, 2, 3], [2, 2, 8], [-3, -10, -2]])
    b = [0, -4, -11]
    L, U = LuUtils.LU(A)
    X = LUsolve(A, b)
    print("L={}".format(L))
    print("U={}".format(U))
    print("X={}".format(X))
    A = np.array([[3, 2, 1, 1], [6, -2, 3, 1], [-5, 10, 1, -1], [1, -1, 1, 1]])
    b = [3.8, 6.1, -1.2, 1.1]
    L, U = LuUtils.LU(A)
    X = LUsolve(A, b)
    print("L={}".format(L))
    print("U={}".format(U))
    print("X={}".format(X))


if __name__ == '__main__':
    getSlove()
