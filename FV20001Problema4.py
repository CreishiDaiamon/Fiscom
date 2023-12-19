

#Utilice el método de Newton-Raphson para calcular r numéricamente con una precisión 10−6

import numpy as np
#Constantes
G=6.674e-11
m=7.348e22
M= 5.974e24
R= 3.844e8
omega=2.662e-6

eps= 1e-6
#Dwfinición de la función
def func(r):
  return (G*M)/r**2-(G*m)/(R-r)**2-omega**2*r

h = 0.05
#definición de derivada
def dev(r):
  return (func(r + h/2) - func(r - h/2)) / h

def newton(r):
  r=0.000001
  delta=1
  while abs(delta)>eps:
    delta= func(r)/dev(r)
    r= r- delta
  return r
valor=newton(0.5)
print("El valor es de:", "{0:1.4f}" .format(valor) )