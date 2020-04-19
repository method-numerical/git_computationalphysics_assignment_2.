import numpy as np 
import scipy.integrate as i
import matplotlib.pyplot as plt 

def f4(t,y):
  return np.cos(2*t)+np.sin(3*t)
n=i.solve_ivp(f4,[0,1],[1],t_eval=np.linspace(0,1)) 

plt.plot(n.t,n.y[0],label='numerical solution of Q7(d).') 
plt.plot(n.t,np.sin(2*n.t)/2-np.cos(3*n.t)/3+4/3,'+',label='analytic solution=sin(2t)/2-cos(3t)/3+4/3.')    
plt.xlabel('t.')
plt.ylabel('y.')
plt.legend();plt.show() 