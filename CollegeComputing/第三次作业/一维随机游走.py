import random
import math
import numpy as np


def random_walk(N, T):
    positions = [0 for i in range(N)]
    for step in range(T):
        x = 0
        for p in range(N):
            coin = random.randint(1, 2)
            if coin == 1:
                positions[p] += 1
            elif coin == 2:
                positions[p] -= 1
        # positions.append(x)
    return np.mean(positions), np.std(positions)


def random_walk_vec(N, T):
    positions = np.zeros(N)
    moves = np.random.randint(1, 3, size=(T, N))
    moves = 2 * moves - 3
    for n in range(T):
        positions += moves[n, :]
    return np.mean(positions), np.std(positions)


def atest_random_walk(N, T):
    print("粒子数:%d, 模拟步数:%d" % (N, T))
    print("位置平均值:%g, 位置标准差:%g" % random_walk(N, T))
    print("向量化模拟的位置平均值:%g, 位置标准差:%g" % random_walk_vec(N, T))
    print()


if __name__ == '__main__':
    random.seed(10)
    np.random.seed(10)
    atest_random_walk(100, 100)
    atest_random_walk(100, 1000)
    atest_random_walk(1000, 1000)
