import numpy as np 
import scipy.integrate as i
import matplotlib.pyplot as plt 

def f2(t,y):
  return 1-(t-y)**2
n=i.solve_ivp(f2,[2,3],[1],t_eval=np.linspace(2,3)) 

plt.plot(n.t,n.y[0],label='numerical solution of Q7(b).') 
plt.plot(n.t,n.t+1/(n.t-3),'+',label='analytic solution=t+1/(t-3).')    
plt.xlabel('t.')
plt.ylabel('y.')
plt.legend();plt.show() 