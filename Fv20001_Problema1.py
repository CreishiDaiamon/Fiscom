import numpy as np
import matplotlib.pyplot as plt
#Se define la función a trabajar
def f(x,x_m):
    return 1/(np.sqrt(np.sin(x_m/2)**2-np.sin(x/2)**2))
#Integración trapecio

#Intervalos
x_m = np.empty(50, dtype="float")
x_m[0]=0.01
i = 1
while i < 50:
    try:
        x_m[i] = x_m[i-1]+0.0626
    except ValueError:
        print("No ha ingresado un número válido. Inténtelo de nuevo.")
    else:
        i += 1
x_1=0
x_2=0.999*x_m
N=100
def trapecio(F,xmin,xmax, Num):
  h=(xmax-xmin)/Num
  s=0.5*F(xmin,x_m)+0.5*F(xmax,x_m)
  for k in range(1,Num):
    s=s+F(xmin+k*h,x_m)
  return h*s
#Integración simpson
def simpson(G,xmin,xmax,Num):
  h2=(xmax-xmin)/(Num-1)
  s2=G(xmin,x_m)+G(xmax,x_m)
  for k in range (1,Num-1):
    if k%2==0:
      s2=s2+4*G(xmin+k*h2,x_m)
    else:
      s2=s2+2*G(xmin+k*h2,x_m)
  return h2*s2/3

Trapecio1=(1/np.pi)*trapecio(f,x_1,x_2,N)

Simpson1=(1/np.pi)*simpson(f,x_1,x_2,N)

#b)
def g(x):
  return 1+((1/2)**2)*(np.sin(x/2))**2+((3)/(8)**2)*(np.sin(x/2))**4
calc=g(x_m)

f, ax = plt.subplots(1,figsize=(10,10))
plt.plot(x_m,Trapecio1, "bo", label=r'$Método$ $Trapecio$')
plt.plot(x_m,Simpson1, "go", label=r'$Método$ $Simpson$')
plt.plot(x_m,calc, label=r'$Serie$', color="red")

ax.legend(loc='upper left',prop={'size':15})

ax.set_xlabel(r'$\theta_m$',fontsize=10) 
ax.set_ylabel(r'$T/T_o$',fontsize=10) 

f.savefig('Oscilaciones pequeñas por integracion.png', dpi=300)
plt.show()

