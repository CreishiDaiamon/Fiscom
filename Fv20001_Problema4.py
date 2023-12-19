import numpy as np
import matplotlib.pyplot as plt
def f1(X,N):
    return (1-X**2)**(N+0.5)

def chev(F,n,x,h):
    s=1
    for k in range(1,2*n+2):
        if k%2!=0:
            s=s*k
    C=((-1)**n*(n+1))/(s*((1-x**2)**0.5))
    if n==1:
        return C*(F(x+0.5*h,n)-F(x-0.5*h,n))/h
    if n==2:
        return C*(F(x+h,n)-2*F(x,n)+F(x-h,n))/h**2
    if n==3: 
        return C*(F(x+1.5*h,n)-3*F(x+0.5*h,n)+3*F(x-0.5*h,n)-F(x-1.5*h,n))/h**3
def dev(F,n,x,h):
    if n==1:
        return (F(x+0.5*h,n)-F(x-0.5*h,n))/h
    if n==2:
        return (F(x+h,n)-2*F(x,n)+F(x-h,n))/h**2
    if n==3: 
        return (F(x+1.5*h,n)-3*F(x+0.5*h,n)+3*F(x-0.5*h,n)-F(x-1.5*h,n))/(h**3)

dev1=dev(f1,1,0.5,0.05)
dev2=dev(f1,2,0.5,0.0005)
dev3=dev(f1,3,0.5,0.0005)
print("La derivada con N=1 es:")
print(dev1)
error1=(-1.299-dev1)/1.299*100
print("y su error es:")
print(error1)
print("La derivada con N=2 es:")
print(dev2)
error1=(dev2)*100
print("y su error es:")
print(error1)
print("La derivada con N=3 es:")
print(dev3)
error1=(22.73316-dev3)/22.73316*100
print("y su error es:")
print(error1)

T = np.linspace(-0.99,0.99,40)

y1=chev(f1,1,T,0.05)
y2=chev(f1,2,T,0.05)
y3=chev(f1,3,T,0.05)
f, ax = plt.subplots(1,figsize=(10,10))
ax.set_facecolor('gray')
for axis in ['top', 'bottom', 'left', 'right']:
  ax.spines[axis].set_color('green')

plt.plot(T,y1, "purple", label=r'$N=1$')
plt.plot(T,y2, "aqua", label=r'$N=2$')
plt.plot(T,y3, label=r'$N=3$', color="green")
plt.grid()

ax.legend(loc='upper left',prop={'size':15})

ax.set_xlabel(r'$x$',fontsize=10) 
ax.set_ylabel(r'$U_n$',fontsize=10) 

f.savefig('PolinomiosdelChe.png', dpi=300)
plt.show()