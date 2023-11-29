import numpy as np
import aux_functions as aux

# Paso 1 simular de integral de E(f(t)^{2}), f(t)=B_{t}
n = 1000
n2 = 100
time = 1
t,w = aux.strong_brownian(time,n)
w2 = w**2
mean = t
integral = time**2/2

# Paso 2 simular la E(|I(f)|^{2})
#calcular el I(f) 
E_If = 0
for j in range(n2):
   I_fn = 0
   for i in range(n):
      I_fi= t[i-1]*(w[i]-w[i-1])
      I_fn += I_fi
   I_f=I_fn**2
   E_If += I_f
   
E_If = 1/n2*E_If
print(integral)
print(E_If)









