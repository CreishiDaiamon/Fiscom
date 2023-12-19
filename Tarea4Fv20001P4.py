import matplotlib.pyplot as plt
import numpy as np

def simulacion_decaimiento(N, P, tmax):
    # Lista para almacenar el número de partículas en cada paso de tiempo
    particulas = [N]

    # Simulamos el decaimiento hasta tmax
    for t in range(1, tmax+1):
        # Contamos el número de partículas que decaen en este paso de tiempo
        decaimientos = np.sum(np.random.rand(particulas[-1]) < P)
        
        # Calculamos el nuevo número de partículas después del decaimiento
        particulas_nuevo = particulas[-1] - decaimientos
        
        # Añadimos el nuevo número de partículas a la lista
        particulas.append(particulas_nuevo)

    return particulas

# Parámetros
P = 0.005
tmax = 500
valores_N = [10, 100, 1000, 10000, 100000]

# Graficamos la simulación para diferentes valores de N
for N in valores_N:
    resultados = simulacion_decaimiento(N, P, tmax)
    plt.plot(range(tmax+1), resultados, label=f'N = {N}')

plt.title('Simulación de Decaimiento Radiactivo')
plt.xlabel('Tiempo')
plt.ylabel('Número de Partículas')
plt.legend()
plt.show()