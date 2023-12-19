import numpy as np
from scipy.constants import h

hbarc=0.1973 #eV*micrometros
m=0.511e6 #eV/c^2
V=20 #eV
w=1e-3 #micrometros

def y1(E):
  return np.tan(np.sqrt((w**2*m*E)/(2*hbarc**2)))

def y2(E):
  return np.sqrt((V-E)/E)

def y3(E):
  return -np.sqrt(E/(V-E))


a=np.arange(0.1,V,0.1)

import matplotlib.pyplot as plt


plt.plot(a,y1(a))
plt.plot(a,y2(a))
plt.plot(a,y3(a))
plt.ylim(-25,25)

print("Los primeros 5 estados excitados obsevando la gráfica son:  1.2, 2.5, 5, 7.8, 11.2$ (eV)")

def bisection (xminus, xplus, f, Nmax, eps):
  i=0
  x=xplus
  while abs(f(x))> eps  and i < Nmax :
    x=(xplus + xminus)/2.0                             

    if (f(xplus)*f(x) > 0.0 ) :
      xplus=x
    else:
      xminus=x
    i+=1
  if i == Nmax:
    print ( f" Raíz no encontrada despues de {Nmax} iteraciones \n" )
  else:
    print(f"\n Raiz: {x}, con un error de: {eps} , y {i} iteraciones\n")
  return x

def fp(E): #Pares
  return y1(E)-y2(E)

def fi(E): #Impares
  return y1(E)-y3(E)

E1=bisection(1,2.5,fi,1000, 0.001)
E2=bisection(2.5,2.9,fp,1000, 0.001)
E3=bisection(3,5.2,fi,1000, 0.001)
E4=bisection(7,8,fp,1000, 0.001)
E5=bisection(10,12,fi,1000, 0.001)

print("E1 \t E2 \t E3 \t  E4 \t  E5 \t Unidades ")
print("{0:1.2f} \t {1:1.2f} \t {2:1.2f} \t {3:1.2f} \t {4:1.2f} \t eV ".format(E1,E2,E3,E4,E5))
plt.show()