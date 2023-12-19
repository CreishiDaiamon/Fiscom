import numpy as np
#Canmbié la integral a coordenadas polares por lo cual me queda una integral en terminos de r de 0 a infinito multiplicada por pi cuartos
#A LA CUAL LE REALICE CAMBIO DE VARIABLE PARA QUE ME QUEDARA DE 0 A 1
def f(z):
    return np.exp(-z/(1-z))/(1-z)**2
#Definición de los limites evitando indefiniciones
a,b=0.01,0.99
#Metodo de cuarto grado para integración con sus respectivos pesos
def int_cuar(G,xmin,xmax,N):
    h=(xmax-xmin)/(N-1)
    s=14*(G(xmax)+G(xmin))/45
    for k in range(1,N-1):
        if (k%5==0 or k%9==0):
          s=s+(28/45)*G(k*h)
        elif (k%3==0 or k%7==0):
           s=s+(8/15)*G(k*h)
        else:
           s=s+(64/45)*G(k*h)            
    return s*h
#Valor de la integral
I=int_cuar(f,a,b,30)
#Valor total
Icalc=I*(np.pi/4)
print(I)
print(Icalc)
Re=np.pi/4
#El Resultado real es pi/4 entonces para el error procentural se tiene:
error=(Re-Icalc)/Re*100
print("El error porcentual es de:")
print(error)