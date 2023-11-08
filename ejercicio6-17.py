import numpy as np
import matplotlib.pyplot as plt
import aux_functions as aux


t_final = 1
n_points = 65
delta_t = 1/(n_points - 1)
alpha = 0.7

prng = np.random.RandomState(219)

time, w = aux.strong_brownian(1,n_points) # w_i

y = np.sqrt(delta_t *(alpha - alpha ** 2)) * prng.standard_normal(n_points - 1)  # la variable que completa para que sea movimiento browniano, prng.standard_normal(n_points - 1) es vector de tamaño n-1

w_ = np.roll(w, -1)  # w_i+1, recorer las casillas, el -1 significa que te recorre el del final al primero 

w_alpha = alpha * w_ + (1 - alpha) * w # es un vector que tiene como elementos w_{i+\alpha}
w_alpha = np.delete(w_alpha, -1) # estamos elimando eñ ultimo que no es un incremento del vector W_{\alpha}
w_alpha += y # una manera 
w_ref = np.zeros(2* n_points -1)

w_ref[0::2] = w
w_ref[1::2] = w_alpha

time_ref = np.zeros(2 * n_points - 1)

for i in range(2 * n_points - 1):
    if i % 2 == 0:
        time_ref[i] = time[int(i / 2)]
    else:
        time_ref[i] = time[int(i / 2)] + alpha * delta_t

plt.plot(time_ref,w_ref,'g-')
plt.plot(time, w,'ro')
plt.show()