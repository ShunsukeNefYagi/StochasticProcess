### Poissonノイズの発生時刻
# 指数分布の理論解を用いた Poisson ノイズの数値計算コード
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 18

def path_gen(seed):
    np.random.seed(seed)
    t, events, lmd = 0.0, [], 1.0
    while t < 10.0:
        t += np.random.exponential(1.0/lmd)
        if t < 10.0:
            events.append(t)
    return events
events = path_gen(seed=10)
y = np.zeros(len(events))
plt.scatter(events,y,marker="o",color="red")
plt.show()