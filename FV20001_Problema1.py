import numpy as np
import matplotlib.pyplot as plt
#Definción de funciones----------------------------------------------------------------------------------------------
#Se define una función con las ecuaciones de Lorenz
def Lorenz(sigma, r, b, x, y, z):
    dx_dt = sigma * (y - x)
    dy_dt = r * x - y - x * z
    dz_dt = x * y - b * z
    return dx_dt, dy_dt, dz_dt

# Esat función nos da los nuevos puntos en los que será evaluada la función, estos se obtienen por RK-2
def RK2(sigma, r, b, x, y, z, h):
    k1x, k1y, k1z = Lorenz(sigma, r, b, x, y, z)
    k2x, k2y, k2z = Lorenz(sigma, r, b, x + h * k1x, y + h * k1y, z + h * k1z)

    new_x = x + h * (k1x + k2x) / 2
    new_y = y + h * (k1y + k2y) / 2
    new_z = z + h * (k1z + k2z) / 2

    return new_x, new_y, new_z
#Proceso-------------------------------------------------------------------------------------------------------------------
#Constantes dadas
sigma = 10
r = 28
b = 8/3
condiciones_i = (1, 0, 0)
t_max = 50
h = 0.0005  # Paso temporal

#Listas que almacenarán los resultados del proceso
t_lista = np.arange(0, t_max, h)
x_lista, y_lista, z_lista = [], [], []
# Se definen los valores iniciales de x,y,z
x, y, z = condiciones_i
#Se hacen las iteraciones necesarias para los valores de t con el paso que se escogió
for t in t_lista:
    x_lista.append(x)
    y_lista.append(y)
    z_lista.append(z)
    x, y, z = RK2(sigma, r, b, x, y, z, h)
#Gráficas---------------------------------------------------------------------------------------------------------------
# Grafica y en función del tiempo
plt.plot(t_lista, y_lista, label='y(t)', color="gray")
plt.xlabel('Tiempo')
plt.ylabel('y')

plt.title('Ecuaciones de Lorenz - y(t) vs. Tiempo')
plt.legend()
plt.show()

# Grafica z vs. x (Atractor de Lorenz)
plt.figure()
plt.plot(x_lista, z_lista, label='Atractor de Lorenz', color="lavender")
plt.xlabel('x')
plt.ylabel('z')
plt.title('Atractor de Lorenz')
plt.legend()
plt.show()