#Gabriel Sebastíán Flores Ventura FV20001
#Ejercicio 1 Tarea 1; Física computacional

import numpy as np #Tratado de datos y operaciones con los mismos
import matplotlib.pyplot as plt #Librería que hace posible la graficación de los datos
import scipy as sc # se usa Scipy para aprovechar su constante almacenada
import os #se usa para determinar la existencia del archivo

D=np.loadtxt('sunmod.dat')#Lectura del archivo
atcap,logtauR, lgTau5k, T,Pe=D[:,0],D[:,1],D[:,2],D[:,3], D[:,4]#Asignación de los datos del archivo a sus respectivas variables


#Densidad electrónica de electrones de cada capa
Eld=Pe/(sc.constants.Boltzmann*T)#Cálculo de la densidad electrónica

#creación del archivo ".dat"
if os.path.exists("Densidades.dat"):
  print("El archivo existe" "\n")
  np.savetxt("Densidades.dat",Eld)
  f = open("Densidades.dat")
  f.close()
else:
  print("El archivo no existe y será creado")#La idea de este if else es que al principio cree un archivo y sin necesidad de abrirlo, nos diga si existe o no
  f = open("Densidades.dat", "x")
  f.close()


#Gráfica
f, ax = plt.subplots(1,figsize=(5,5))
plt.plot(T,Eld, label=r'$Densidad$ $electrónica$ $vs$ $temperatura$')
ax.legend(loc='upper right',prop={'size':10})
ax.set_xlabel(r'$Temperatura$',fontsize=10)
ax.set_ylabel(r'$Densidad$ $Electrónica$',fontsize=10)
f.savefig('densidad electrónica.png', dpi=300)# Se guarda el archivo png co su respectivo nombre
plt.show()
#Trabajo testeado en un notebook de Google Colab y posterior depuración en VS Code