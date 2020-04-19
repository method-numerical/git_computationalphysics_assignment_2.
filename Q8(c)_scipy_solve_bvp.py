import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as i

x=np.linspace(np.pi/4,np.pi/3)

y=2*np.ones([2,x.size])

y[0,0]=1/2**0.25
y[0,-1]=12**0.25/2

def f(x,y):
  return np.vstack((y[1],-(2*y[1]**3+y[0]**2*y[1])/np.cos(x))) 
def bc(ya,yb):
  return np.array([ya[0]-1/2**0.25,yb[0]-12**0.25/2])

answer=i.solve_bvp(f,bc,x,y)

plt.plot(x,answer.sol(x)[0],label='numerical solution of Q8(c).') 
plt.plot(x,np.sin(x)**(1/2),'+',label='analytical solution= {sin(x)}^(1/2).')
plt.xlabel('x.'); plt.ylabel('y.')
plt.legend(); plt.show() 