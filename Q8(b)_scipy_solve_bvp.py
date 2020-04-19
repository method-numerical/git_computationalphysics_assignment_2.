import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as i

x=np.linspace(0.01,np.pi/2)

y=2*np.ones([2,x.size]); y[0,0]=1; y[0,-1]=np.e 

def f(x,y):
  return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0]))) 

def bc(ya,yb):
  return np.array([ya[0]-1,yb[0]-np.e]) 

answer=i.solve_bvp(f,bc,x,y)

plt.plot(x,answer.sol(x)[0],label='numerical solution of Q8(b).') 
plt.plot(x,np.exp(np.sin(x)),'+',label='analytical solution= e^(sin(x)).')
plt.xlabel('x.')
plt.ylabel('y.')
plt.legend()
plt.show() 