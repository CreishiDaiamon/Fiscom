import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

#Asignación de los intervalos
T = np.empty(98, dtype="float")
T[0]=10
i = 1
while i < 98:
    try:
        T[i] = T[i-1]+5
    except ValueError:
        print("No ha ingresado un número válido. Inténtelo de nuevo.")
    else:
        i += 1


#Función
def f(x):
    return ((x**4)*(np.exp(x)))/((np.exp(x)-1)**2)
#Metódo cúbico con sus respectivos pesos
def int_cub(F,xmin,xmax,N):
    h=(xmax-xmin)/(N-1)
    s=3*(F(xmax)+F(xmin))/8
    for k in range(1,N-1):
        if k%3==0:
           s=s+(3/4)*F(k*h)
        else:
            s=s+(9/8)*F(k*h) 
    return s*h
TD=428
a,b=0.01,TD/T
N=50
I=int_cub(f,a,b,N)
V=0.001
p=6.022e28
Kb=sc.constants.Boltzmann
Cv=9*V*p*Kb*I*(T/TD)**3

f, ax = plt.subplots(1,figsize=(10,10))
plt.plot(T,Cv, "green", label=r'$Capacidad$ $Calorífica$')


ax.legend(loc='upper left',prop={'size':15})

ax.set_xlabel(r'$T(K)$',fontsize=10) 
ax.set_ylabel(r'$Cv$',fontsize=10) 

f.savefig('CvVSTplot.png', dpi=300)
plt.show()

