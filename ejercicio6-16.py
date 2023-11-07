import numpy as np
import aux_functions as aux
import matplotlib.pyplot as plt

def b_function(t, a, w):
    y = np.exp(t- a * w)
    return y


n_samples = 10000
n_points = 64
t_initial = 0
t_final = 1

mean = np.zeros(n_points)
for i in range(n_samples):
    time, b_w = aux.strong_brownian(t_final,n_points)
    y = b_function(time,0.25, b_w)
    if i < 10:
        plt.plot(time,b_w,'g-',alpha = 0.5)
    mean += y

mean = (n_samples)**(-1) * mean
time = np.linspace(0,t_final, n_points)

y = [np.exp(33 / 32 * t) for t in time]
plt.plot(time, mean, 'r-')
plt.plot(time, y,'b-',alpha = 0.3)
plt.show()
