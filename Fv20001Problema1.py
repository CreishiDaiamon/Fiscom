import numpy as np
import matplotlib.pyplot as plt
D=np.loadtxt('señal1.dat')#Lectura del archivo
t,s=D[:,0],D[:,1]
g1,eje=plt.subplots(1,figsize=(8,5))
plt.title('Señal vs tiempo')
plt.plot(t,s, linestyle='-',color="gray")
eje.set_xlabel(r'$t(s)$', fontsize=10)
eje.set_ylabel(r'$s$', fontsize=10)

plt.show()
print("")
#b)función para obtener TDF
def TDF(y):
  N=len(y)
  c=np.zeros(N//2+1, complex)
  for k in range (N//2+1):
    for n in range (N):
      c[k]+=y[n]*np.exp(-2j*np.pi*k*n/N)
  return c
ck=TDF(s)

#Usando numpy.fft+
ck1=np.fft.fft(s)
g2,eje=plt.subplots(1,figsize=(8,5))
plt.title('Fourier Discreta')
eje.set_xlabel(r'$Frecuencia$', fontsize=10)
eje.set_ylabel(r'$C_k$', fontsize=10)

plt.plot(np.arange(0,len(ck))/2,abs(ck), color="aqua") #L=2
#plt.xlim(0,15)

plt.show()
plt.show()
print("")
g3,eje=plt.subplots(1,figsize=(8,5))
plt.title('Fourier Discreta con Numpy')
eje.set_xlabel(r'$Frecuencia$', fontsize=10)
eje.set_ylabel(r'$C_k$', fontsize=10)
plt.plot(np.arange(0,len(ck1))/2,abs(ck1), color="purple") #L=2
plt.show()
print("")
print("Observando los resulatdos, las frecuencias principales estimadas son: 2 Hz, 5 Hz, 15 Hz")
ckf=np.zeros(len(ck1), complex)
for k in range (len(ck)):
  if k==2*15:# freq=k/L L=2
    ckf[k]=ck[k]

g3,eje=plt.subplots(1,figsize=(8,5))
plt.title('Señal con los filtros aplicados')
eje.set_xlabel(r'$Frecuencia$', fontsize=10)
eje.set_ylabel(r'$C_k$', fontsize=10)
plt.plot(np.arange(0,len(ckf))/2,abs(ckf),'m')

yf=np.fft.ifft(ckf)
g1,eje=plt.subplots(1,figsize=(8,5))
plt.title('Señal vs tiempo')
plt.plot(t,s,'c')
plt.plot(np.arange(0,2,0.01),np.real(yf),'g' )
eje.set_xlabel(r'$t(s)$', fontsize=10)
eje.set_ylabel(r'$s$', fontsize=10)
plt.show()



#f
#Observando el gráfico, obentemos dos puntos:
frecuencia=15.12
x_values = np.array([0, 0.25])
y_values = np.array([0, -2.9])

k=2*np.pi*frecuencia
#Ya que en x=0 y=0, se propone una función seno
#Al resolver la función
A=y_values[1] / np.sin(k * x_values[1])
x = np.linspace(0, 2, 1000)
f11=A*np.sin(k*x)
g5,eje=plt.subplots(1,figsize=(8,5))
plt.title('Señal representada por función analítica')
plt.plot(x,f11, linestyle='-', color="green")

#Ya que k=2*pi/T, T=2pi/k
T=2*np.pi/k
print("El periodo es ",T, k)
plt.show()