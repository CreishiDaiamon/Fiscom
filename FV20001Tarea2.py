#Gabriel Sebastián Flores Ventura FV2001
#Tarea 2 Fis Computacional 1
import numpy as np
x0=np.array([0.5, 0.5,0.5,0.5,0.5,0.5,1,1,1 ],float)
a1,a2,a3,a4,a5,a6,a7,a8,a9=x0
N=len(x0)
er=1e-4
#Funciones del 1 al 9
def f1(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return 3*a1+4*a2+4*a3-8

def f2(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return 3*a4+4*a5-4*a6

def f3(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a1**2+a4**2-1

def f4(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a2**2+a5**2-1

def f5(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a3**2+a6**2-1

def f6(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a7*a4-a8*a5-10

def f7(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a7*a1-a2*a8

def f8(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a8*a5+a9*a6-20

def f9(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    return a8*a2-a3*a9
#Función que evalua funciones(solo evalua las fiunciones en los puntos para obtener el vector de funciones)
def ef(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    fcs = [f1(a1,a2,a3,a4,a5,a6,a7,a8,a9), f2(a1,a2,a3,a4,a5,a6,a7,a8,a9), f3(a1,a2,a3,a4,a5,a6,a7,a8,a9), f4(a1,a2,a3,a4,a5,a6,a7,a8,a9), f5(a1,a2,a3,a4,a5,a6,a7,a8,a9), f6(a1,a2,a3,a4,a5,a6,a7,a8,a9), f7(a1,a2,a3,a4,a5,a6,a7,a8,a9), f8(a1,a2,a3,a4,a5,a6,a7,a8,a9), f9(a1,a2,a3,a4,a5,a6,a7,a8,a9)]
    return fcs
#Función para calcular Jacobiana(aquí se deriva con diferencias centradas y se obtiene la jacobiana a la vez)
def calcular_jacobiana(funcs, d):
    n = len(funcs)
    m = len(d)
    J = np.zeros((n, m))
    for i, func in enumerate(funcs):
        for j, var in enumerate(d):
            # Calcular las derivadas parciales utilizando diferencias centradas
            h = 1e-5  # Tamaño del paso para la diferencia finita
            x_plus_h = np.copy(d)
            x_minus_h = np.copy(d)
            x_plus_h[j] += h
            x_minus_h[j] -= h
            J[i, j] = (func(*x_plus_h) - func(*x_minus_h)) / (2 * h)
    return J
#Función para arreglar diagonales
def fix2(jc,fcs,x):
    while np.any(np.diag(jc) == 0):
        for m in range(N):
            if jc[m,m] == 0:
                for k in range(N):
                    if jc[k,m] != 0:
                        # Intercambiar las filas m y k
                        jc[[m, k], :] = jc[[k, m], :]
                        fcs[m], fcs[k] = fcs[k], fcs[m]
    return jc

#Eliminación Gaussiana
def Eg(j):
    for m in range(N):

    # Dividir los elementos de la diagonal
        div = j[m,m] 
        j[m,:] /= div 
        fcs[m] /= div 

    #Restar los elementos 
        for i in range(m+1,N): 
            mult = j[i,m] 
            j[i,:] -= mult*j[m,:] 
            fcs[i] -= mult*fcs[m] 
# Sustitución 
    x= np.empty(N) 
    for m in range(N-1,-1,-1): 
        x[m] = fcs[m] 
        for i in range(m+1,N): 
            x[m] -= j[m,i]*x[i] 
    return x
#Dos maneras de calculas la magnitud de deltax, (solo usé una función, pero dejo ambas como ambas alternativas)
def magdx(x,y):
    xo=0
    for k in range (N):
        x0=(x[k]-y[k])**2
        return np.sqrt(x0)
def magdx2(x):
    xo=0
    for k in range (N):
        x0=(x[k])**2
        return np.sqrt(x0)
#Proceso
fcs=ef(a1,a2,a3,a4,a5,a6,a7,a8,a9)#Vector de funciones evaluadas
funcs = [f1, f2, f3, f4, f5, f6, f7, f8, f9]#Vector de funciones
jc = calcular_jacobiana(funcs, x0)#calculo de la Jacobiana
jp= fix2(jc,fcs,x0)#Arregla las diagonales intercambiando las filas de manera que no queden diagonales nulas 
x= np.empty(N)
x=Eg(jp)#Crea el array con los delta x
x1=x0-x#Calcula el nuevo X
md=magdx(x1,x0)#Esta linea y la posterior poseen la misma función de calcular la magnitud del vector delta x
md2=magdx2(x)
b1,b2,b3,b4,b5,b6,b7,b8,b9=x1#Asignación de los nuevos puntos a sus respectivas variables
x0=x1#Asigna los nuevos puntos encontrado como los puntos con los que se va a trabajar

print("Tablas de valores:")
print("dx \t cosθ1 \t\t cosθ2 \t \t cosθ3 \t\t  senθ1 \t  senθ2 \t  senθ3 \t  T1 \t\t  T2 \t\t  T3")
print("{0:1.4f} \t {1:1.4f} \t {2:1.4f} \t {3:1.4f} \t {4:1.4f} \t {5:1.4f} \t {6:1.4f} \t {7:1.4f} \t {8:1.4f} \t {9:1.4f}".format(md,b1,b2,b3,b4,b5,b6,b7,b8,b9))
#Iteraciones
while (md>er):
    fcs=ef(b1,b2,b3,b4,b5,b6,b7,b8,b9)
    jc = calcular_jacobiana(funcs, x0)
    jp= fix2(jc,fcs,x0)
    x=Eg(jp)
    x1=x0-x
    md=magdx(x1,x0)
    b1,b2,b3,b4,b5,b6,b7,b8,b9=x1
    x0=x1
    print("{0:1.4f} \t {1:1.4f} \t {2:1.4f} \t {3:1.4f} \t {4:1.4f} \t {5:1.4f} \t {6:1.4f} \t {7:1.4f} \t {8:1.4f} \t {9:1.4f}".format(md,b1,b2,b3,b4,b5,b6,b7,b8,b9))

t1=np.arccos(b1)*57.29#valores de los ángulos convertidos a Grados
t2=np.arcsin(b5)*57.29
t3=np.arccos(b3)*57.29

print("θ1 \t θ2 \t θ3 \t  T1 \t  T2 \t  T3")
print("{0:1.2f} \t {1:1.2f} \t {2:1.2f} \t {3:1.2f} \t {4:1.2f} \t {5:1.2f} ".format(t1,t2,t3,b7,b8,b9))
#Trabajo hecho en VScode
    