"""
-fang zen
"""


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
            return FMatrix(self.n,result)
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
                        num += self.data[i][n]*o_cols[j][n]

                    row.append(num)
                result.append(row)
            return FMatrix(self.n,result)
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


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 6, 7], [0, 0, 1]]
    B = [[1, 2, 3], [4, 6, 7], [1, 0, 0]]

    C = FMatrix(3,A)
    D = FMatrix(3,B)
    E = C+D
    print(C.transpose())