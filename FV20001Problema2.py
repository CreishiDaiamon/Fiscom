import numpy as np
def f(x):
    return 5*np.exp(-x)+x-5

def bisec(xminus,xplus,Nmax,eps):
    for k in range(0,Nmax):
        x = (xminus + xplus)/2 
        print("x:",x,"f(x)",f(x))
        if f(xplus)*f(x) > 0:
            xplus = x
        else:
            xminus = x
        if abs(f(x)) < eps:
            print("Raiz encontrada",eps)
            break
        if k == Nmax-1:
            print("No se encontró la raíz")
    return x

print(f(4),f(6))

x = bisec(4,6,100,1E-6)
h = 6.62607E-34 #en J*s
c = 3E8 #en m/s
k_B =  1.38E-23 #en J/K
#La constante de Wein se obtiene despejando b=hc/xk_B

b = (h*c)/(x*k_B)

print("b=",b,"mK")

#Literal b

T = 5778 #Kelvin
lon = b/T #longitud de onda
v = c/lon #frecuencia

print("La frecuencia es",v,"Hz")