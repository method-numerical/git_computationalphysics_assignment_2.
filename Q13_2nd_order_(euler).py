import numpy as np 
import matplotlib.pyplot as plt  
 
h=0.001 
t=np.linspace(1,2,int(1/h+1))
y=7*t/4+t**3*np.log(t)/2-3*t**3/4 
w=np.zeros([len(t),2]) 
w[0]=[1,0] 
 
def f(t,y): 
  return np.array([y[1],t*np.log(t)-2*y[0]/t**2+2*y[1]/t]) 
 
for j in range(len(t)-1): 
  w[j+1]=w[j]+h*f(t[j],w[j])
 
plt.plot(t,w[:,0],'c',label='numerical_solution.') 
plt.plot(t,y,'--',linewidth=4,label='true_solution.') 
plt.xlabel('t.') 
plt.ylabel('y.') 

plt.legend() 
plt.show() 