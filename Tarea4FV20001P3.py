import matplotlib.pyplot as plt
import random

def camino_aleatorio(N):
    # Inicializamos las posiciones iniciales
    x_actual, y_actual = 0, 0

    # Listas para almacenar las posiciones en cada paso
    x_posiciones = [x_actual]
    y_posiciones = [y_actual]

    # Realizamos N pasos del camino aleatorio
    for _ in range(N):
        # Generamos desplazamientos aleatorios en las direcciones x e y
        desplazamiento_x = random.uniform(-1, 1)
        desplazamiento_y = random.uniform(-1, 1)

        # Actualizamos las posiciones
        x_actual += desplazamiento_x
        y_actual += desplazamiento_y

        # Agregamos las nuevas posiciones a las listas
        x_posiciones.append(x_actual)
        y_posiciones.append(y_actual)

    return x_posiciones, y_posiciones

# Diferentes valores de N
valores_N = [100, 200, 300, 400]

# Graficamos los caminos aleatorios para cada valor de N
for N in valores_N:
    x, y = camino_aleatorio(N)
    plt.plot(x, y, label=f'N = {N}')

plt.title('Simulación de Caminos Aleatorios')
plt.xlabel('Posición en X')
plt.ylabel('Posición en Y')
plt.legend()
plt.show()