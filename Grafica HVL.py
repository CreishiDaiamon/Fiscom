import numpy as np
import matplotlib.pyplot as plt
a,b=[0,0.1,0.5,1,3,4],[1,0.97,0.87,0.78,0.52,0.44]
x,y=np.array(a),np.array(b)
ly=np.log(y)
print(ly)
xp,yp,Cxx,Cxy,Sxx=0,0,0,0,0 #Contadores
N=len(y) #Número de datos
def prom(a,c): #Función promedio
  for k in range(0,N):
    c=c+a[k]
  return c/N
Exp=prom(x,xp)#promedio x
Eyp=prom(ly,yp)#promedio y

for k in range(0,N): #Cálculo de E_{xy}
  Cxy=Cxy+x[k]*ly[k]
Exy=Cxy/N


for k in range(0,N): #Cálculo de E_{xx}
  Cxx=Cxx+x[k]*x[k]
Exx=Cxx/N

m=(Exy-Exp*Eyp)/(Exx-Exp*Exp) #Cálculo de la pendiente
c=(Exx*Eyp-Exp*Exy)/(Exx-Exp*Exp)#Cálculo del intercepto
ec=np.exp(c)
for k in range(0,N): #Cáculo de X^2
  Sxx=Sxx+(m*x[k]+c-y[k])*(m*x[k]+c-y[k])

print(m,ec,Sxx)
x1=m*x
print(x1)
y1=ec*np.exp(x1)

#Gráfica 
f, ax = plt.subplots(1,figsize=(5,5))
plt.plot(x,y, "bo", label=r'$Datos$ $medidos$')#Se generan los puntos que representan las mediciones del problema
plt.plot(x,y1,":", label=r'$Ajuste$ $Mínimos$', color="red")#Se genera la recta de ajuste

ax.legend(loc='upper right',prop={'size':5})#Tamaño y posición de la leyenda

ax.set_xlabel(r'$mmAl$',fontsize=10) #Leyenda variable independiente
ax.set_ylabel(r'$Transmisión$',fontsize=10) #Leyenda variable dependiente

f.savefig('graficaHVL.png', dpi=300)#Se guarda la g´rafica con el nombre asignado
plt.show()
#Trabajo testeado en un notebook de Google Colab y posterior depuración en VS Code