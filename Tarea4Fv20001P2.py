import random
import numpy as np
def integrando(x):
    return 4 / (1 + x**2)

def montecarlo_integration(num_puntos):
    suma = 0

    for _ in range(num_puntos):
        x = random.uniform(0, 1)
        suma += integrando(x)

    resultado_estimado = suma / num_puntos

    # Calcula la incerteza
    suma_cuadrados = sum((integrando(random.uniform(0, 1)) - resultado_estimado)**2 for _ in range(num_puntos))
    incerteza = (suma_cuadrados / num_puntos)**0.5

    return resultado_estimado, incerteza

# Valores de N para la simulación Montecarlo
valores_N = [1000, 10000, 100000, 1000000]

for N in valores_N:
    resultado_estimado, incerteza = montecarlo_integration(N)
    print(f"N = {N}:")
    print(f"Resultado estimado: {resultado_estimado}")
    print(f"Incerteza: {incerteza}")
    print()

# Valor de π de Python
valor_pi_python = np.pi
print(f"Valor de π en Python: {valor_pi_python}")