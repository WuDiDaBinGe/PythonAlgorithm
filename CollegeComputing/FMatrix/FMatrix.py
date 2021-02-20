"""
方阵
"""
class FMatrix(object):
    ######### Begin #########








    ########## End ##########
    

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