import numpy as np
def dentro_del_hemisferio(x, y, z):
    return x**2 + y**2 + z**2 <= 1
from pylab import plot,show 
N=500
a = 1664525 
c = 1013904223 
m = 4294967296 
x=1 
results = [] 
#Se crea una lista con numeros pseudorandoms
for i in range(N): 
    x = (a*x+c)%m
    results. append(x/(m-1)) 

def volumen_hemisferio_montecarlo(num_puntos):
    puntos_dentro = 0

    for i in range(num_puntos):
        x = results[i]
        y = results[i]
        z = results[i]

        if dentro_del_hemisferio(x, y, z):
            puntos_dentro += 1

    proporcion_puntos_dentro = puntos_dentro / num_puntos

    # Volumen del cubo unitario
    volumen_cubo = 1**3

    # Estimación del volumen del hemisferio
    volumen_hemisferio_estimado = 4*proporcion_puntos_dentro * volumen_cubo

    # Volumen real del hemisferio
    volumen_hemisferio_real = (2/3)*np.pi

    return volumen_hemisferio_estimado, volumen_hemisferio_real

volumen_estimado, volumen_real = volumen_hemisferio_montecarlo(N)

print("Volumen estimado del hemisferio:", volumen_estimado)
print("Volumen real del hemisferio:", volumen_real)
error=(abs(volumen_real-volumen_estimado)/volumen_real)*100
print("Error:", error)