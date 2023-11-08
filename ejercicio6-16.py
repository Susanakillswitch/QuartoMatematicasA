import numpy as np
import aux_functions as aux
import matplotlib.pyplot as plt

def b_function(t, a, w): # y local va dentro de una funcion
    y = np.exp(t+ a * w)
    return y


n_samples = 10000
n_points = 64
t_initial = 0
t_final = 1

mean = np.zeros(n_points) # la esperanza es una funcion, es la media de la muestra para cada t, para cada t fija se tiuene una variable aleatoria.
for i in range(n_samples):
    time, b_w = aux.strong_brownian(t_final,n_points) # la time es la t y b_w es la w de los valores que te regresa la funcion
    y = b_function(time,0.25, b_w) # y global va en el codigo principal y es distinta a la de arriba, aqui y es un vector de exponenciales y b_w es la trayectoria del proceso w_{i} el valor de w al tiempo i w_{t} la trayectoria
    if i < 10:
        plt.plot(time,b_w,'g-',alpha = 0.5) # que me grafique hasta la trayectoria 10
    mean += y # el vector de la esperanza le sumas el nuevo en cada 1

mean = (n_samples)**(-1) * mean # promediendo
time = np.linspace(0,t_final, n_points)

y = [np.exp(33 / 32 * t) for t in time] # el valor vedadero
plt.plot(time, mean, 'r-', alpha = 0.5)
plt.plot(time, y,'b-',alpha = 0.3)
plt.show()
