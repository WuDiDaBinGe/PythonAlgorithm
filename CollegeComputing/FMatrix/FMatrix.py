"""
方阵
"""
import random
class FMatrix(object):
    ######### Begin #########








    ########## End ##########

    def __str__(self):
        tmpStr = ''
        for i in range(self.n):
            row_str = map(lambda x: str(x), self.data[i])
            tmpStr += '\t'.join(row_str) + '\n'
        return tmpStr


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