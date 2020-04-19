import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as i

x=np.linspace(1,2)

y=2*np.ones([2,x.size])

y[0,0]=0
y[0,-1]=np.log(2) 

def f(x,y):
  return np.vstack((y[1],-np.exp(-2*y[0]))) 
def bc(ya,yb):
  return np.array([ya[0]-0,yb[0]-np.log(2)])

answer=i.solve_bvp(f,bc,x,y)

plt.plot(x,answer.sol(x)[0],label='numerical solution of D²y=-e^-2y,y(1)=0,y(2)=ln2.') 
plt.plot(x,np.log(x),'+',label='analytical solution= ln(x).')
plt.xlabel('x.'); plt.ylabel('y.')
plt.legend(); plt.show() 