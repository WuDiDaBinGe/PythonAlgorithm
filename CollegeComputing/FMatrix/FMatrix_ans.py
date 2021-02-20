"""
方阵
"""
import random


class FMatrix(object):
    def __init__(self, n, data):
        self.n = n
        self.data = data

    def __add__(self, other):
        if self.n == other.n:
            result = []
            for i in range(0, self.n):
                row = []
                for j in range(0, self.n):
                    row.append(self.data[i][j] + other.data[i][j])
                result.append(row)
            return FMatrix(self.n, result)
        else:
            return "Wrong Computed!"

    def __sub__(self, other):
        if self.n == other.n:
            if self.n == other.n:
                result = []
                for i in range(0, self.n):
                    row = []
                    for j in range(0, self.n):
                        row.append(self.data[i][j] - other.data[i][j])
                    result.append(row)
                return FMatrix(self.n, result)
        else:
            return "Wrong Computed!"

    def __mul__(self, other):
        if self.n == other.n:
            result = []
            o_cols = [list(row) for row in zip(*other.data)]
            for i in range(self.n):
                row = []
                for j in range(self.n):
                    num = 0
                    for n in range(self.n):
                        num += self.data[i][n] * o_cols[j][n]
                    row.append(num)
                result.append(row)
            return FMatrix(self.n, result)
        else:
            return "Wrong Computed!"

    def __str__(self):
        tmpStr = ''
        for i in range(self.n):
            row_str = map(lambda x: str(x), self.data[i])
            tmpStr += '\t'.join(row_str) + '\n'
        return tmpStr

    def transpose(self):
        cols = [list(row) for row in zip(*self.data)]
        return FMatrix(self.n, cols)


def test_ans():
    random.seed(88)
    for count in range(4):
        n = random.randint(2, 5)
        data_A = [[random.randint(-100, 100) for i in range(n)] for j in range(n)]
        data_B = [[random.randint(-100, 100) for i in range(n)] for j in range(n)]
        A = FMatrix(n, data_A)
        B = FMatrix(n, data_B)
        print(A.transpose())
        print(B.transpose())
        print(A+B)
        print(A-B)
        print(A*B)
    data_A = [[random.randint(-100, 100) for i in range(3)] for j in range(3)]
    data_B = [[random.randint(-100, 100) for i in range(2)] for j in range(2)]
    A = FMatrix(3, data_A)
    B = FMatrix(2, data_B)
    print(A.transpose())
    print(B.transpose())
    print(A + B)
    print(A - B)
    print(A * B)

test_ans()