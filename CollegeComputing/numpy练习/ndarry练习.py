import numpy as np
import numpy.linalg  as la


# 用numpy.random模块的randint函数
# 构造一个由[-5, 5]之间的随机整数构成的n*n矩阵
def get_random_matrix(n):
    ######### Begin #########
    arry = np.random.randint(-5, 6, size=(n, n))
    A = np.asmatrix(arry)
    return A
    ########## End ##########


# 根据公式，计算矩阵M的Moore Penrose逆矩阵
def moore_penrose_inverse(M):
    ######### Begin #########
    u, d, v = la.svd(M)
    u = u.H
    v = v.H
    d = 1 / d
    d = np.diag(d)
    d = d.T
    d = d.conj()
    return (v * d * u)

    ########## End ##########


# 把moore_penrose_inverse函数的计算结果
# 与linalg模块的pinv函数返回值进行比较
# 返回两个矩阵各元素误差的绝对值的最大值
def compare_with_pinv(M, MPI):
    ######### Begin #########
    return np.max(abs(la.pinv(M) - MPI))

    ########## End ##########


if __name__ == '__main__':
    np.random.seed(0)
    n = eval(input())
    M = get_random_matrix(n)
    print(repr(M))
    MPI = moore_penrose_inverse(M)
    print(MPI)
    print("最大误差：%g" % compare_with_pinv(M, MPI))
