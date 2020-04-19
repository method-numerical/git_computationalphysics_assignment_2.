import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1,100)
y=np.zeros([len(x),2]) 

def f(y,x):
  t=y[1]
  u=x*np.exp(x)-x-y[0]+2*y[1]
  return np.array([t,u])
  
for j in range(len(x)-1):
  h=x[1]-x[0] 
  k1=h*f(y[j],x[j])
  k2=h*f(y[j]+k1/2,x[j]+h/2)
  k3=h*f(y[j]+k2/2,x[j]+h/2)
  k4=h*f(y[j]+k3,x[j]+h)
  y[j+1]=y[j]+(k1+2*k2+2*k3+k4)/6

plt.plot(y[:,0],label='D²y-D¹y+y=xe^x-x.')

plt.xlabel('x.')
plt.ylabel('y.')
plt.legend()
plt.show()

