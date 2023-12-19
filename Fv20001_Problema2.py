import numpy as np
import matplotlib.pyplot as plt
#definición de funciones----------------------------------------------------------------------
# Ecuaciones diferenciales del tiro parabólico con resistencia al aire dadas
def proyectil(t, r, k, n):
    x, y, vx, vy = r
    v = np.sqrt(vx**2 + vy**2)
    ax = -k * v**n * vx / v
    ay = -9.81 - k * v**n * vy / v
    return [vx, vy, ax, ay]

# Método de Runge-Kutta de orden 4
def RK4(func, t, r, h, k, n):
    k1 = h * np.array(func(t, r, k, n))
    k2 = h * np.array(func(t + 0.5*h, r + 0.5*k1, k, n))
    k3 = h * np.array(func(t + 0.5*h, r + 0.5*k2, k, n))
    k4 = h * np.array(func(t + h, r + k3, k, n))
    return r + (k1 + 2*k2 + 2*k3 + k4) / 6

# Solución analítica para el caso sin fricción (tiro parabólico)
def analitica(t, v0x, v0y):
    x = v0x * t
    y = v0y * t - 0.5 * 9.81 * t**2
    return x, y
#Proceso------------------------------------------------------------------------------------------
# Parámetros
k = 0.8
v0x = 18.23
v0y = 12.3
x0 = 0
y0 = 0
n_lista = [1, 3/2, 2]
t_max = 25
h = 0.01

# Listas que almacenarán los resultados
t_lista = np.arange(0, t_max, h)
x_lista, y_lista = {}, {}
vx_lista, vy_lista, v_lista = {}, {}, {}

# Resolver las ecuaciones para cada valor de n
for n in n_lista:
    r = np.array([x0, y0, v0x, v0y])
    x_vals, y_vals = [], []
    vx_vals, vy_vals, v_vals = [], [], []
    
    for t in t_lista:
        x_vals.append(r[0])
        y_vals.append(r[1])
        vx_vals.append(r[2])
        vy_vals.append(r[3])
        v_vals.append(np.sqrt(r[2]**2 + r[3]**2))
        
        r = RK4(proyectil, t, r, h, k, n)
    
    x_lista[n] = x_vals
    y_lista[n] = y_vals
    vx_lista[n] = vx_vals
    vy_lista[n] = vy_vals
    v_lista[n] = v_vals

# Graficas----------------------------------------------------------------------------
plt.figure()
#Soluciones para cada n
for n, x_vals, y_vals in zip(n_lista, x_lista.values(), y_lista.values()):
    plt.plot(x_vals, y_vals, label=f'n={n}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trayectorias del tiro parabólico con resistencia al aire')
plt.legend()

# Solución analiticas
x_an, y_an = analitica(t_lista, v0x, v0y)
plt.plot(x_an, y_an, label='Sin Resistencia al aire', linestyle='dashed')

# Se establecen límites en x e y para mejor visualización
plt.xlim(left=0, right=50)
plt.ylim(bottom=0, top=np.max(y_an))

plt.legend()
plt.show()

# Grafica de velocidades en función del tiempo
plt.figure()
for n, v_vals in v_lista.items():
    plt.plot(t_lista, v_vals, label=f'n={n}')
plt.xlabel('Tiempo')
plt.ylabel('|v|')
plt.title('Velocidades en función del tiempo para diferentes valores de n')
plt.legend()
plt.show()