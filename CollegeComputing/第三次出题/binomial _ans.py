import random
import math
import numpy as np


def s_binomial(p, n, x):
    return (math.factorial(n) / (math.factorial(x) * math.factorial(n - x))) * math.pow(p, x) * math.pow(1 - p, n - x)


def simulate_binomial(p, n, x, N):
    M = 0
    for i in range(N):
        m = 0
        for j in range(n):
            q = random.random()
            if q <= p:
                m += 1
        if m == x:
            M += 1
    return M / N, abs(M / N-s_binomial(p, n, x))


def simulate_binomial_np(p, n, x, N):
    M = 0
    q_list = np.random.random((N, n))
    success = q_list <= p
    for i in range(N):
        if np.sum(success[i]) == x:
            M += 1
    return M / N


def testfunction():
    print("第一个测试用例：")
    a = s_binomial(1 / 2, 5, 2)
    b, err = simulate_binomial(1 / 2, 5, 2, 10000000)
    print("accuracy:%g, estimate:%g, error:%g"%(a ,b ,err))
    # print(simulate_binomial_np(1 / 2, 5, 2, 10000000))

    print("第二个测试用例：")
    a = s_binomial(5 / 6, 4, 4)
    b, err = simulate_binomial(5 / 6, 4, 4, 10000000)
    print("accuracy:%g, estimate:%g, error:%g"%(a ,b ,err))
    # print(simulate_binomial_np(5 / 6, 4, 4, 10000000))

    print("第三个测试用例：")
    a = s_binomial(11 / 120, 5, 3)
    b, err = simulate_binomial(11 / 120, 5, 3, 10000000)
    print("accuracy:%g, estimate:%g, error:%g"%(a ,b ,err))
    # print(1 - simulate_binomial_np(1 / 120, 5, 0, 10000000))


testfunction()