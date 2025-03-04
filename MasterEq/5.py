### Poisson ノイズに駆動される確率過程
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 18

def path_gen(seed):
    ts = np.linspace(0,10.0,1000)
    v, vs, dt, lmd, y = 0.0, [], ts[1] - ts[0], 0.5, 1.0
    np.random.seed(seed)
    for t in ts:
        vs.append(v)
        if lmd * dt >= np.random.rand():
            v += y
        v += - v * dt
    return vs, ts
vs, ts = path_gen(2)
plt.plot(ts, vs)
plt.show()