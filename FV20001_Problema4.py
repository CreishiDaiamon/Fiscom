
import numpy as np 
num_puntos = 10**6
radio = 1.0
#hago uso de numpy.uniform mporque incluye ambops límites 0 y 1
#Funciones-------------------------------------------------------------------------------------
def dentro_del_hemisferio(x,y,z,w):
  return x**2+y**2+z**2+w**2<=1
#Calculo de A
A=2**5 #(b-a)^k siendo k el número de variables
def Esti_volumen(num_puntos):
  puntos_dentro=0
  for _ in range(num_puntos):
    #Se asignan valores random a las variables
    x=np.random.uniform(0,1)
    y=np.random.uniform(0,1)
    z=np.random.uniform(0,1)
    w=np.random.uniform(0,1)
    #Con la función se verifica que os puntos esten dentro y si lo estan se agrega 1 al contador de puntos dentro
    if dentro_del_hemisferio(x,y,z,w):
      puntos_dentro+=1
    volumen= 16*puntos_dentro/num_puntos*(1)**3 #El 16 es explicado al final de todo el código
  return volumen

def montecarlo5(N):
    integral_sum = 0
    
    for _ in range(N):
        u = np.random.uniform(-1, 1)
        v = np.random.uniform(-1, 1)
        w = np.random.uniform(-1, 1)
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        
        integrando = ((2 + u + v) / (5 + w + x)) ** y
        integral_sum += integrando
    
    #Promedio
    integral_estimada = A*integral_sum / N
    
    return integral_estimada

#Proceso---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
N1 = 10**4 #Intenté con potencias de 7 y 8 pero el tiempo de cálculo es demasiado al menos para mi comoputadora e incluso en Collab, la configuracion que tarda menos de un minuto es esta
N2 = 10**5
#N1=10**7
#N2=10**8
##Estimado de alpha
alpha=Esti_volumen(num_puntos)/np.pi # Se divide entre pir porque lo que se obtiene en realidad es el volumen
#y como r es unitario no se agraga así obtenemos la constante alpha necesaria

# Calculo de la integral de 5 dimensiones para N1 y N2
integral_N1 = montecarlo5(N1)
integral_N2 = montecarlo5(N2)

#Resultados
print(f"Estimación de la constante alpha para una 3-esfera: {alpha:.4f}")
print(f"Resultado de la integral para N1={N1}: {integral_N1:.6f}")
print(f"Resultado de la integral para N2={N2}: {integral_N2:.6f}")

#Explicación de porque multiplico por 16.
#En la tarea 4, hay un ejercicio de cálcaular el volumen de una semiesfera o semihemisferio, en la cual nos indica como calcularlo
#Y en la misma tarea nos dice que multipliquemos por 4, a lo cual me pregunté porqué, lo que sucede es que
# para ello se toman los puntos que caen dentro de 1 de los cuatro cuadrantes (esto se da por elevar al cuadrado las variables, 
#o también podria decirse que por la raiz cuadrada) superiores de un mapa 3D por asi decirlo, con esto no se
#toman en cuenta los otros 3 cuadrantes, por lo tanto en 3D existen 4 cuadrantes para una semiesfera de los ccuales solo se toma en cuenta
#1 es decir un cuarto de toda la semiesfera, por lo cual si yo quisiera obtener el volumen de la semiesfera tendria que multiplicar por 4
# y si quisiera el de toda la esfera seria por 8 (4x2), que sucede en el caso de la 3-esfera, se agrega y una nueva variable que añade dos
#dos posibilidades nuevas de signo, positivo y negativo, por lo cual con la condición de el cuadrante solo estariamos tomando 1 de 16 "cuadrantes" posibles
#por que los "cuadrantes" de la semi esfera superior ya no serian 4 sino que 4x2=8 y para la esfera completa, 8x2=16.
# con este razonamiento se puede obtener el alfa de la 2-esfera y la 1-esfera(Obviamente reduciendo el número de variables en la condición del "cuadrante") 
# lo cual uso como prueba de que esta hipótesis es correcta.