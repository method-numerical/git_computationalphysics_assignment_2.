import numpy as np
import scipy.optimize as o
import matplotlib.pyplot as plt 

def ivp(f,y_a):
  h=x[1]-x[0]
  w=y_a*np.ones(len(x))
  for j in range(len(x)-1):
    def g(r):
      return w[j]+h*f(r,x[j+1])-r
    w[j+1]=o.newton(g,0.1)
  return w

def f1(y,x):
  return -9*y
def f2(y,x):
  return -20*(y-x)**2+2*x

x= np.linspace(0,1,100)

plt.plot(x,ivp(f1,np.e),label='y=-9y.') 
plt.plot(x,ivp(f2,1/3),label='y=-20(y-x)^2+2x.') 

plt.xlabel('x.')
plt.ylabel('y.')
plt.legend() 
plt.show() 
