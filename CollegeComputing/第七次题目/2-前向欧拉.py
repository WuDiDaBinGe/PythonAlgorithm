# import ode_7 as ode
import numpy as np


def myprint_list(l):
    if type(l) != list:
        print('Error: the result is not a list')
    else:
        print('[', end='')
        for i in range(len(y_f) - 1):
            print("%.4f, " % y_f[i], end='')
        print("%.4f]" % y_f[len(y_f) - 1])


class SIR():
    def __init__(self, beta, gamma, y0):
        self.beta = beta
        self.gamma = gamma
        self.y0 = y0  # 参数属性

    def f(self, y):  # y为当前状态，即列表[S,I,R]
        # ------------------begin-----------------------
        S = y[0]; I = y[1]; R = y[2]
        return [-self.beta * S * I, self.beta * S * I - self.gamma * I, self.gamma * I]
        # -------------------end------------------------

    def solve(self, t):
        # ------------------begin-----------------------
        result = []
        result.append(self.y0[1])
        y = [self.y0.copy()] * len(t)
        for i in range(len(t) - 1):
            dt = t[i + 1] - t[i]
            cnt = self.f(y[i])
            y[i + 1][0] = y[i][0] + dt * cnt[0]
            y[i + 1][1] = y[i][1] + dt * cnt[1]
            y[i + 1][2] = y[i][2] + dt * cnt[2]
            result.append(y[i + 1][1])
        # -------------------end------------------------
        return result


N = 1e8  # 武汉总人数：1000万人
gamma = 1 / 25  # 假设肺炎平均25天治愈（15天潜伏+10天治疗）
y0 = [N - 1, 1, 0]  # 初始发病1人，其他人员正常, 即[S0, I0, R0]
beta = 1.0 / N  # 感染系数
simulation = SIR(beta=beta, gamma=gamma, y0=y0)
for T in [5, 10, 20]:
    t = range(0, T, 1)  # 模拟T天的发展情况，单位时间为1天
    y_f = simulation.solve(t)
    myprint_list(y_f)