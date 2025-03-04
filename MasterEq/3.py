### Poissonノイズの発生時刻
# 愚直に計算する方法
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 18

def path_gen(seed):
    np.random.seed(seed)
    ts = np.linspace(0, 10.0, 1000)
    events, dt, lmd = [], ts[1] - ts[0], 1.0
    for t in ts:
        if lmd * dt > np.random.rand():
            events.append(t)
    return events
events = path_gen(seed = 100)
y = np.zeros(len(events))
plt.scatter(events, y, marker="o", color = "red")
plt.show()