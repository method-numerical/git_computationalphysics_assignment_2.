import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as i

x=np.linspace(0,np.pi)

y=2*np.ones([2,x.size]); y[0,0]=2; y[0,-1]=2

def f(x,y):
  return np.vstack((y[1],(1-y[1]**2-y[0]*np.sin(x))/2))  

def bc(ya,yb):
  return np.array([ya[0]-2,yb[0]-2]) 

answer=i.solve_bvp(f,bc,x,y)

plt.plot(x,answer.sol(x)[0],label='numerical solution of Q8(d).') 
plt.plot(x,2+np.sin(x),'+',label='analytical solution= 2+sin(x).')
plt.xlabel('x.')
plt.ylabel('y.')
plt.legend()
plt.show() 