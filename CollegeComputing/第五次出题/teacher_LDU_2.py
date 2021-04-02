import numpy as np


class LUDecompose:
    def __init__(self, A, b):
        self._A = np.array(A, dtype=np.float64)
        self._b = np.array(b, dtype=np.float64)
        self._size = self._b.size

    # 对系数矩阵进行LU分解，返回L矩阵（ndarrray类型）
    # 注意需要考虑对角线元素为0的情况
    def decompose(self):
        n = self._size
        A = self._A
        for i in range(n):
            for j in range(i, n):
                if i ==j:
                    flag = sum([A[i, k] * A[k, j] for k in range(i)])
                    # 处理0
                    if flag == A[i, j]:
                        index = 0
                        maxnum = 0
                        for row in range(i+1, n):
                            if maxnum < abs(A[row, j]):
                                maxnum = abs(A[row, j])
                                index = row
                        # 交换两行
                        A[[i, index], :] = A[[index, i], :]
                        # 交换 b
                        self._b[i], self._b[index] = self._b[index], self._b[i]
                t = sum([A[i, k] * A[k, j] for k in range(i)])
                A[i, j] = A[i, j] - t

            for j in range(i + 1, n):
                t = sum([A[j, k] * A[k, i] for k in range(i)])
                A[j, i] = (A[j, i] - t) / A[i, i]
        self._A = A
        L = np.eye(n)
        for i in range(n):
            for j in range(i):
                L[i, j] = A[i, j]
        return L

    # 在LU分解的基础上，求解并返回方程组的根（ndarray类型）
    def solve(self):
        n = self._size
        y = np.zeros(n)
        for i in range(n):
            t = sum([self._A[i, j] * y[j] for j in range(i)])
            y[i] = self._b[i] - t
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            t = sum([self._A[i, j] * x[j] for j in range(i, n)])
            x[i] = (y[i] - t) / self._A[i, i]
        return x



if __name__ == '__main__':
    A = eval(input())
    b = eval(input())
    lud = LUDecompose(A, b)
    print("分解后的L矩阵：")
    print(lud.decompose())
    print("方程组根：", lud.solve())
