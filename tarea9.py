import numpy as np
##import aux_functions as aux
##import matplotlib.pyplot as plt
# Paso 1 simular de integral de E(f(t)^{2}), f(t)=B_{t}
#n = 500
#n2 = 500
#time=1

# w2 = w**2
# mean = t
#integral1 = time**3/3########
#def strong_brownian(t, n): #Moviento browniano con la normal
    #dt = t / n
   # dw = np.zeros(n)##########
    #w = np.zeros(n)
    #for i in np.arange(1, n):
        #dw[i] = np.sqrt(dt)*np.random.standard_normal()
        #w[i] = w[i - 1] + dw[i]
   # time = np.linspace(0, t, n)
   # return time, w

###########
# Paso 2 simular la E(|I(f)|^{2})
#calcular el I(f) 
#E_If = 0
#for j in range(n2):
   #I_fn = 0
   #t,w = strong_brownian(time, n)
   #for i in range(n-1):
      #I_fi= t[i]*(w[i+1]-w[i])
      #I_fn += I_fi
   #I_f = I_fn ** 2
   #E_If += I_f

#print(n2 ** (-1) * E_If)
#print(integral1)

import numpy as np
import aux_functions as aux

n = 500
n2 = 500
time=1
integral1 = time**3/3

def strong_brownian(t, n): 
    dt = t / n
    dw = np.zeros(n)
    w = np.zeros(n)
    for i in np.arange(1, n):
        dw[i] = np.sqrt(dt)*np.random.standard_normal()
        w[i] = w[i - 1] + dw[i]
    time = np.linspace(0, t, n)
    return time, w

E_If = 0
for j in range(n2):
   I_fn = 0
   t,w = strong_brownian(time, n)
   for i in range(n-1):
      I_fi= t[i]*(w[i+1]-w[i])
      I_fn += I_fi
   I_f = I_fn ** 2
   E_If += I_f

print(n2 ** (-1) * E_If)
print(integral1)

#"calculando la integral de Itô del movimiento Browniano W(t).py"
import numpy as np


def f(x: float, t: float):
    y = x
    return y
     

def fB(partition: np.array, x: float, t: float):
    y = 0
    for i in range(len(partition) - 1):
        if partition[i] <= t < partition[i + 1]:
            y = f(x, t)
    return y

def ito_n(n_points: int, t: float):
    time, w = bw.u(t, n_points)
    integral = np.zeros(n_points)
    for i in range(n_points - 1):
        integral[i] = fB(time, w[i], time[i]) * (w[i + 1] - w[i])
    ito = integral.sum()
    return w, ito





