#Gabriel Sebastíán Flores Ventura FV20001
#Ejercicio 2 Tarea 1; Física computacional
import numpy as np # Se importa numpy para trabajar los datos
import matplotlib.pyplot as plt #Librería que hace posible la graficación de los datos
#Lectura de datos del  fichero
D=np.loadtxt('datos.dat')
#Asignación de los datos leídos a variables de tipo lista
x,y=D[:,0],D[:,1]

xp,yp,Cxx,Cxy,Sxx=0,0,0,0,0 #Contadores
N=len(y) #Número de datos

def prom(a,c): #Función promedio
  for k in range(0,N):
    c=c+a[k]
  return c/N

Exp=prom(x,xp)#promedio x
Eyp=prom(y,yp)#promedio y


for k in range(0,N): #Cálculo de E_{xy}
  Cxy=Cxy+x[k]*y[k]
Exy=Cxy/N


for k in range(0,N): #Cálculo de E_{xx}
  Cxx=Cxx+x[k]*x[k]
Exx=Cxx/N


m=(Exy-Exp*Eyp)/(Exx-Exp*Exp) #Cálculo de la pendiente


c=(Exx*Eyp-Exp*Exy)/(Exx-Exp*Exp)#Cálculo del intercepto


for k in range(0,N): #Cáculo de X^2
  Sxx=Sxx+(m*x[k]+c-y[k])*(m*x[k]+c-y[k])

print(m,c,Sxx)

y1=m*x+c #Asignación de la función de ajuste de mínimos

#Gráfica 
f, ax = plt.subplots(1,figsize=(5,5))
plt.plot(x,y, "bo", label=r'$Datos$ $medidos$')#Se generan los puntos que representan las mediciones del problema
plt.plot(x,y1,":", label=r'$Ajuste$ $Mínimos$', color="red")#Se genera la recta de ajuste

ax.legend(loc='upper right',prop={'size':5})#Tamaño y posición de la leyenda

ax.set_xlabel(r'$x$',fontsize=10) #Leyenda variable independiente
ax.set_ylabel(r'$y$',fontsize=10) #Leyenda variable dependiente

f.savefig('ajuste_por_mínimos_cuadrados.png', dpi=300)#Se guarda la g´rafica con el nombre asignado
plt.show()
#Trabajo testeado en un notebook de Google Colab y posterior depuración en VS Code