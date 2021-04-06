# -*- coding : utf-8 -*-
# coding: utf-8
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 采用matplotlib作图时默认设置下是无法显示中文的，凡是汉字都会显示成方块。
# 实际上，matplotlib是支持unicode编码的，不能正常显示汉字主要是没有找到合适的中文字体。
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示问题
matplotlib.rcParams['axes.unicode_minus'] = False


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
t = range(0, 60, 1)  # 模拟60天的发展情况，单位时间为1天
simulation = SIR(beta=beta, gamma=gamma, y0=y0)
y1 = simulation.solve_with_quarantine(t)
y2 = simulation.solve_with_quarantine(t, 1/15)
y3 = simulation.solve_with_quarantine(t, 1/3)
# ------------------begin-----------------------
#1. 设置图形大小
plt.figure(figsize = (10, 8))
#2. 绘制曲线：横轴是时间/天，纵轴是感染人数
tt = [i for i in range(60)]
plt.plot(tt, y1)
plt.plot(tt, y2)
plt.plot(tt, y3)
#3. 设置图题'未隔离与隔离机制下新冠病毒发展趋势对比分析'、
#   横轴标签'时间/天'、纵轴标签'人数'、
#   图列说明('未实施隔离', '确诊隔离', '疑似隔离', 分别对应三条曲线)
plt.title("未隔离与隔离机制下新冠病毒发展趋势对比分析")
plt.xlabel("时间/天")
plt.ylabel("人数")
plt.legend(['未实施隔离',  '确诊隔离', '疑似隔离'])
# ------------------end-----------------------

# 设置y轴刻度
Vy = [1.0e6, 5.0e6] + [i * 1.e7 for i in range(11)]
plt.yticks(Vy, ['%d' % e for e in Vy])

plt.savefig('src/step6/student/result.png')
