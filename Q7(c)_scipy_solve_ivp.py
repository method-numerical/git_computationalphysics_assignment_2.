import numpy as np 
import scipy.integrate as i
import matplotlib.pyplot as plt 

def f3(t,y):
  return 1+y/t 
n=i.solve_ivp(f3,[1,2],[2],t_eval=np.linspace(1,2)) 

plt.plot(n.t,n.y[0],label='numerical solution of Q7(c).') 
plt.plot(n.t,n.t*np.log(n.t)+2*n.t,'+',label='analytic solution=tln(t)+2t.')    
plt.xlabel('t.')
plt.ylabel('y.')
plt.legend();plt.show() 