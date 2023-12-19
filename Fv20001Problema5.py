import numpy as np 
import matplotlib.pyplot as plt

def f(x,y):
    return y**2-2*y+x**4-2*x**2+x

figura=plt.figure()

ax = plt.axes(projection='3d')


xmin=-1.5
xmax=1.5
ymin=0
ymax=2

X=np.linspace(xmin,xmax,40)
Y=np.linspace(ymin,ymax,40)
#Crear la malla 
X,Y=np.meshgrid(X,Y)
#definir Z
Z=f(X,Y)
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot_wireframe(X,Y,Z, color="black")

#primeros puntos vistos del minimo con la grafica
x0=[-1,1]



#calculo de gradientes
def gradx(F,x,y,h):
    return (F(x+0.5*h,y)-F(x-0.5*h,y))/h
def grady(F,x,y,h):
    return (F(x,y+0.5*h)-F(x,y-0.5*h))/h
#Cálculo de segunda derivadas
def segundadevx(F,x,y,h):
    return (F(x+h,y)-2*F(x,y)+F(x-h,y))/h**2
def segundadevy(F,x,y,h):
    return (F(x,y+h)-2*F(x,y)+F(x,y-h))/h**2

def newton_raphson (x0, tol, max_iter):
    #Se establecen las variables a utilizar en la función.
    a=x0
    x = a[0]
    y=a[1]
    error = np.inf
    for i in range (max_iter):
        #Calcular el gradiente y el Hessiano, se almacenan los valores en listas debido a que en la matriz Hessian no puedo ponerle de input los valores de x y y nuevos

        g=[gradx(f,x,y,0.05),grady(f,x,y,0.05)]
        sd=[segundadevx(f,x,y,0.05),segundadevy(f,y,x,0.05)]

        H = np.array ( [[sd[0], 0], [0, sd[1]]])
        #Verificar que la matriz sea invertible
        if np.linalg.det (H) == 0:
            print ("La Hessiana tiene una singularidad en", x)
            break
        # Se cambia el punto usando la ecuacción de Newton-Raphson
        a = a - np.linalg.inv (H) @ g #mulptiplicación de matrices
        x = a[0]
        y=a[1]
        #Calcula el error como la norma del gradiente
        error = np.linalg.norm (g)
        #Imprime la iteración, punto y error correspondiente
        print ("Iteración", i+1, ": x,y =", a, ", error =", error)
        #Verificar que el error sea menor a la tolerancia
        if error < tol:
            print ("Converge al punto mínimo")
            break
    #Se retornan los valores finales de los puntos y la función
    return a, f (a [0], a [1])
#primeros puntos vistos del minimo con la grafica
x0=[-1,1]
tol = 1e-6

#Se aplica el método de Newton Raphson y se almacenan los datos de los puntos donde ocurre el mínimo y el valor de la función en el mínimo
x_min, f_min = newton_raphson (x0, tol, 100)

# Se imprimen los resultados
print ("El primer punto mínimo es", x_min)
print ("El valor en el primer mínimo es", f_min)
#Se aplica el método de Newton Raphson y se almacenan los datos de los puntos donde ocurre el mínimo y el valor de la función en el mínimo
#segundos puntos vistos desde la gráfica
x0=[1,1]
x_min, f_min = newton_raphson (x0, tol, 100)

#Se imprimen los resultados.
print ("El segundo punto mínimo es", x_min)
print ("El valor en el segundo mínimo es", f_min)
plt.show()