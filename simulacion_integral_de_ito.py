import numpy as np

T = 1.0
L = 2**13
dt = T / L
dW = np.sqrt(dt) * np.random.normal(size=L)
W = np.zeros(L + 1)
W[1 :] = np.cumsum(dW)
ito_integral = np.sum(np.multiply(W[0: -1], dW))
err = np.abs(ito_integral - 0.5 * (W[-1] ** 2 - T))
print(err)
# integral de stratonovich
def bw(t: float, n: int):
    dt = t / (n - 1)
    dw = np.sqrt(dt) * np.random.standard_normal(n - 1)
    w = np.zeros(n)
    w[1:] = dw.cumsum()
    time = np.linspace(0, t, n)
    return time, w

t_f = 1
n_p = 2** 13
t, wt = bw(t_f, n_p)
y = 0.5 * np.sqrt(t[1] - t[0]) * np.random.standard_normal(n_p)
stratonovich = [(0.5 * (wt[i + 1] + wt[i]) + y[i])* (wt[i + 1] - wt[i]) for i in range(n_p - 1)]
stratonovich = np.array(stratonovich).sum()
print(np.abs(stratonovich - 0.5 * wt[-1] ** 2))