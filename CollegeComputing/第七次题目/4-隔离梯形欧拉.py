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
        self.beta = beta;
        self.gamma = gamma;
        self.y0 = y0  # 参数属性

    def f(self, y):  # y为当前状态，列表[S,I,R]
        S = y[0]
        I = y[1]
        R = y[2]
        return [-self.beta * S * I, self.beta * S * I - self.gamma * I, self.gamma * I]

    def solve_with_quarantine(self, x, gamma=1 / 25):
        # ------------------begin-----------------------
        self.gamma = gamma
        result = []
        result.append(self.y0[1])
        y = [self.y0.copy()] * len(x)
        for i in range(len(x) - 1):
            h = x[i + 1] - x[i]
            cnt_p = self.f(y[i])
            y_p = []
            y_p.append(y[i][0] + h * cnt_p[0])
            y_p.append(y[i][1] + h * cnt_p[1])
            y_p.append(y[i][2] + h * cnt_p[2])
            cnt_c = self.f(y_p)
            y_c = []
            y_c.append(y[i][0] + h * cnt_c[0])
            y_c.append(y[i][1] + h * cnt_c[1])
            y_c.append(y[i][2] + h * cnt_c[2])
            y[i + 1][0] = (y_p[0] + y_c[0]) * 1 / 2
            y[i + 1][1] = (y_p[1] + y_c[1]) * 1 / 2
            y[i + 1][2] = (y_p[2] + y_c[2]) * 1 / 2
            result.append(y[i + 1][1])
        # -------------------end------------------------
        return result



N = 1e8  # 武汉总人数：1000万人
gamma = 1 / 25  # 假设肺炎平均25天治愈（15天潜伏+10天治疗）
y0 = [N - 1, 1, 0]  # 初始发病1人，其他人员正常 [S0, I0, R0]
beta = 1.0 / N  # 平均传染率

for T in [5, 10, 20]:
    t = range(0, T, 1)  # 模拟T天的发展情况，单位时间为1天
    print("———————————— 无隔离下感染情况：————————————")
    simulation = SIR(beta=beta, gamma=gamma, y0=y0)
    y_f = simulation.solve_with_quarantine(t)
    myprint_list(y_f)
    print("———————————— 隔离确诊患者：————————————")
    gamma1 = 1 / 15  # 隔离确诊患者：按最长15天发病确诊后被隔离
    y_f = simulation.solve_with_quarantine(t, gamma1)
    myprint_list(y_f)
    print("———————————— 隔离疑似人员：————————————")
    gamma1 = 1 / 3  # 隔离疑似人员：按平均3天被隔离
    y_f = simulation.solve_with_quarantine(t, gamma1)
    myprint_list(y_f)
