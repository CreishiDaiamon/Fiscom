import numpy as np
import matplotlib.pyplot as plt

def poisson2D(precision, delta_x, delta_y):
    # Parámetros y discretización
    L = 100 # Tamaño de la caja en metros
    rho1 = 1.0  # Densidad de carga positiva en C/m^2(La unidades segun el Mark Newman)
    rho2 = -1.0  # Densidad de carga negativa en C/m^2

    # Número de nodos en x e y
    nx = int(L / delta_x) + 1
    ny = int(L / delta_y) + 1

    #Potencial inicial
    phi = np.zeros((nx, ny))

    # Condiciones de frontera establecidas en el problema
    phi[0, :] = 0  
    phi[:, 0] = 0  

    #Función para obtener la densidad de carga en cada punto
    def densidadcarga(x, y):
        # Verifica si el punto está dentro de las cargas cuadradas
        if 60 <= x <= 80 and 60 <= y <= 80:
            return rho1
        elif 20 <= x <= 40 and 20 <= y <= 40:
            return rho2
        else:
            return 0

    #Iteraciones
    while True:
        phi_new = np.copy(phi)

        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                rho = densidadcarga(i * delta_x,j * delta_y)
                phi_new[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1] - delta_x**2 * rho/permitividad)

        #Se calcula la diferencia para usar como paramétro de convergencia
        max_diff = np.max(np.abs(phi_new - phi))

        #Se actualiza el potencial
        phi = np.copy(phi_new)

        #Se verifica la convergencia
        if max_diff < precision:
            break

    return phi
#Proceso------------------------------------------------------------------------------------------------------------
#Constantes y paramétros
precision = 10**(-2)
delta_x = 1#cm
delta_y = 1#(m)
permitividad=1 #()
#Agrega los valores de phi a uan variable llamada potencial
potencial = poisson2D(precision, delta_x, delta_y)

# Grafica-----------------------------------------------------------------------------------------------
plt.imshow(potencial, origin='lower', cmap='jet')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.title('Potencial en una caja bidimensional')
plt.show()