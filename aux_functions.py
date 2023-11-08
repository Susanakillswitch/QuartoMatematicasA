import numpy as np


def brownian_motion(t_0,t_f,n): #movimiento browniano con la binomial
    delta = (t_f - t_0) / n  # Tamaño de paso
    # eps  = 1.0 / np.sqrt(n)
    eps = np.sqrt(delta) # Recordemos eps^2 = delta
    t = np.linspace(t_0, t_f, n+1)  # Malla de puntos
    b = np.random.binomial(1, 0.5, n) # Bernoulli, 1 es numero de tiros por experimento que seria la n de la binomial, n cuantas veces lo realizamos el tamaño del vedctor.
    omega = 2.0 * b - 1 # indicar si sube o baja sirve para generar el browniano
    xn = eps * (omega.cumsum()) # cumsum es un vector que acomula el actual con el anterior, las historia acomulada, eps=desviacion estandar para preservar el comportamiento de browniano
    xn = np.concatenate(([0],xn)) #al 0 le pegamos el xn
    return t, xn # t es l particion para graficar


def strong_brownian(t, n): #Moviento browniano con la normal
    dt = t / n
    dw = np.zeros(n)
    w = np.zeros(n)
    for i in np.arange(1, n):
        dw[i] = np.sqrt(dt)*np.random.standard_normal()
        w[i] = w[i - 1] + dw[i]
    time = np.linspace(0, t, n)
    return time, w

def scale_brownian(t, n, c): #Moviento escalado
    dt = c**2 * t / n
    dw = np.zeros(n + 1)
    w = np.zeros(n + 1)
    for i in np.arange(1, n):
        dw[i] = np.sqrt(dt)*np.random.standard_normal()
        w[i] = w[i - 1] + dw[i]
    time = c**2 * np.linspace(0, t, n + 1)
    return time, c**(-1) * w

