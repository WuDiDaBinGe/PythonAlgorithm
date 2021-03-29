import numpy as np

"""
4
1 2 1 4
2 0 4 3
4 2 2 1
-3 1 3 2
13
28
20
6
"""


def single_line_elimination(array, N, p, res_array):
    for r in range(p + 1, N):
        m = array[r][p] / array[p][p]
        array[r][p] = 0
        for c in range(p + 1, N + 1):
            array[r][c] = array[r][c] - m * array[p][c]

        res_array[r] = res_array[r] - m * array[p][N]


def many_line_elimination(array, N, res_array):
    for p in range(0, N):
        single_line_elimination(array, N, p, res_array)

    arr = np.zeros((N, N))
    for p in range(0, N):
        for q in range(0, N):
            arr[p][q] = array[p][q]
    return arr


def back_to_generation(first_array, second_array):
    N = len(second_array)
    res = np.zeros((N, 1), dtype=np.double)
    res[N - 1] = second_array[N - 1] / first_array[N - 1, N - 1]
    for k in range(N - 2, -1, -1):
        res[k] = (second_array[k] - np.dot(first_array[k, k + 1:], res[k + 1:])) / first_array[k, k]

    print(res)


def gaussian_elimination(array, N, res_array):
    arr = many_line_elimination(array, N, res_array)
    back_to_generation(arr, res_array)


def main():
    N = int(input())
    array = np.zeros((N, N + 1))
    res_array = np.zeros((N, 1))

    for i in range(0, N):
        input_line = input()
        arr = np.array(list(map(float, input_line.split())))
        for r in range(0, N):
            array[i][r] = arr[r]

    for i in range(0, N):
        input_num = np.double(input())
        array[i][N] = input_num
        res_array[i] = input_num
    gaussian_elimination(array, N, res_array)
    # res = Gussian_dlim(array, res_array)
    # print(res)


def Gussian_dlim(A, b):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if j == i: continue
            coe = A[j][i]/A[i][i]
            for k in range(i, n):
                A[j][k] -= coe*A[i][k]
            b[j] -= coe*b[i]
    return [b[i]/A[i][i] for i in range(n)]


if __name__ == '__main__':
    main()