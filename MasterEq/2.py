### 決定論的常微分方程式
# jump あり

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 18

def path_gen():
    ts = np.linspace(0, 10.0, 1000)
    vs, v, dt, tau, y = [], 1.0, ts[1] - ts[0], 5.0, 1.0
    for t in ts:
        vs.append(v)
        F = y if tau <= t < tau + dt else 0.0
        v += - v * dt + F
    return vs, ts
vs, ts = path_gen()
plt.plot(ts, vs)
plt.show()