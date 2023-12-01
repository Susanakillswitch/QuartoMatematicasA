import numpy as np
import aux_functions as aux
import matplotlib.pyplot as plt
# Paso 1 simular de integral de E(f(t)^{2}), f(t)=B_{t}
n = 500
n2 = 500
time=1

# w2 = w**2
# mean = t
integral1 = time**3/3

# Paso 2 simular la E(|I(f)|^{2})
#calcular el I(f) 
E_If = 0
for j in range(n2):
   I_fn = 0
   t,w = aux.strong_brownian(time, n)
   for i in range(n-1):
      I_fi= t[i]*(w[i+1]-w[i])
      I_fn += I_fi
   I_f = I_fn ** 2
   E_If += I_f

print(n2 ** (-1) * E_If)





