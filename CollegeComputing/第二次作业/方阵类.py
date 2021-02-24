import random


class SquareMatrix(object):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
    ######### Begin #########
        if len(self) == len(other):
            result = []
            for i in range(0, len(self)):
                row = []
                for j in range(0, len(self)):
                    row.append(self.data[i][j] + other.data[i][j])
                result.append(row)
            return SquareMatrix(result)
        else:
            return "Error"
    ########## End ##########

    def __sub__(self, other):

        ######### Begin #########
        if len(self) == len(other):
            result = []
            for i in range(0, len(self)):
                row = []
                for j in range(0, len(self)):
                    row.append(self.data[i][j] - other.data[i][j])
                result.append(row)
            return SquareMatrix(result)
        else:
            return "Error"

    ########## End ##########

    def __mul__(self, other):

        if len(self) == len(other):
            result = []
            o_cols = [list(row) for row in zip(*other.data)]
            for i in range(len(self)):
                row = []
                for j in range(len(self)):
                    num = 0
                    for n in range(len(self)):
                        num += self.data[i][n] * o_cols[j][n]
                    row.append(num)
                result.append(row)
            return SquareMatrix(result)
        else:
            return "Error"

    def __str__(self):
        SMStr = '{'
        for i in range(len(self)):
            SMStr += str(self.data[i])
            SMStr += '\n '
        SMStr += '}'
        return SMStr

    def __len__(self):
        return len(self.data)

######### Begin #########


########## End ##########


def test_SquareMatrix(data_A, data_B):
    A = SquareMatrix(data_A)
    B = SquareMatrix(data_B)
    print('方阵相加结果：')
    print(A + B)
    print('方阵相减结果：')
    print(A - B)
    print('方阵相乘结果：')
    print(A * B)


if __name__ == '__main__':
    random.seed(88)
    for count in range(4):
        n = random.randint(2, 5)
        data_A = [[random.randint(-100, 100) for i in range(n)] for j in range(n)]
        data_B = [[random.randint(-100, 100) for i in range(n)] for j in range(n)]
        test_SquareMatrix(data_A, data_B)
    data_A = [[random.randint(-100, 100) for i in range(3)] for j in range(3)]
    data_B = [[random.randint(-100, 100) for i in range(2)] for j in range(2)]
    test_SquareMatrix(data_A, data_B)

