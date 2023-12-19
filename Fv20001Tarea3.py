import numpy as np
import matplotlib.pyplot as plt

def runge_kutta(h, x, y, vx, vy):
    r = np.sqrt(x**2 + y**2)
    r_cubo = r**3

    k1x = h * vx
    k1y = h * vy
    k1vx = h * (-x / r_cubo)
    k1vy = h * (-y / r_cubo)

    k2x = h * (vx + k1vx / 2)
    k2y = h * (vy + k1vy / 2)
    k2vx = h * (-(x + k1x / 2) / (r + k1x / 2)**3)
    k2vy = h * (-(y + k1y / 2) / (r + k1y / 2)**3)

    k3x = h * (vx + k2vx / 2)
    k3y = h * (vy + k2vy / 2)
    k3vx = h * (-(x + k2x / 2) / (r + k2x / 2)**3)
    k3vy = h * (-(y + k2y / 2) / (r + k2y / 2)**3)

    k4x = h * (vx + k3vx)
    k4y = h * (vy + k3vy)
    k4vx = h * (-(x + k3x) / (r + k3x)**3)
    k4vy = h * (-(y + k3y) / (r + k3y)**3)

    new_x = x + (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    new_y = y + (k1y + 2 * k2y + 2 * k3y + k4y) / 6
    new_vx = vx + (k1vx + 2 * k2vx + 2 * k3vx + k4vx) / 6
    new_vy = vy + (k1vy + 2 * k2vy + 2 * k3vy + k4vy) / 6

    return new_x, new_y, new_vx, new_vy
#Ejcución de todas las iteraciones
def iteraciones(N, tmax):
    h = tmax / N
    t_valores = np.linspace(0, tmax, N+1)
    x_valores = np.zeros(N+1)
    y_valores = np.zeros(N+1)
    vx_valores = np.zeros(N+1)
    vy_valores = np.zeros(N+1)

    # Condiciones iniciales
    t_valores[0] = 0
    x_valores[0] = 0.5
    y_valores[0] = 0
    vx_valores[0] = 0
    vy_valores[0] = 1.65

    for i in range(1, N+1):
        t_valores[i] = t_valores[i-1] + h
        x_valores[i], y_valores[i], vx_valores[i], vy_valores[i] = runge_kutta(h,
                                                                          x_valores[i-1], y_valores[i-1],
                                                                          vx_valores[i-1], vy_valores[i-1])

    return t_valores, x_valores, y_valores, vx_valores, vy_valores

# Parámetros
N = 10000
tmax = 210

#Encontrando los valores de velocidad y posición con respecto del tiempo
t_valores, x_valores, y_valores, vx_valores, vy_valores = iteraciones(N, tmax)

# Gráfica la órbita calculada en el plano x, y
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(x_valores, y_valores, label='Órbita del cometa')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Órbita del cometa en el plano x, y')
plt.legend()

# Gráfica la velocidad del cometa en función del tiempo
plt.subplot(1, 2, 2)
plt.plot(t_valores, np.sqrt(vx_valores**2 + vy_valores**2), label='Velocidad del cometa')
plt.xlabel('Tiempo')
plt.ylabel('Velocidad')
plt.title('Velocidad del cometa en función del tiempo')
plt.legend()

plt.tight_layout()
plt.show()
plt.show()
