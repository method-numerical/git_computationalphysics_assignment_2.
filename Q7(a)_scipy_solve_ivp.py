import numpy as np 
import scipy.integrate as i
import matplotlib.pyplot as plt 

def f1(t,y):
  return t*np.exp(3*t)-2*y 
n=i.solve_ivp(f1,[0,1],[0],t_eval=np.linspace(0,1)) 

plt.plot(n.t,n.y[0],label='numerical solution of Q7(a).') 
plt.plot(n.t,((5*n.t-1)*np.exp(3*n.t)+np.exp(-2*n.t))/25,'+',label='analytic solution=((5t-1)*e^(3t)+e^(-2t))/25.')    
plt.xlabel('t.')
plt.ylabel('y.')
plt.legend();plt.show() 