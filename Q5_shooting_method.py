import numpy as np
import scipy.optimize as o 
import matplotlib.pyplot as plt

t=np.linspace(0,10,40)
h=t[1]-t[0] 
w=np.zeros([len(t),2])

def f(y,t):
  return np.array([y[1],-10])
  
def k(w_a):
  w[0,1]=w_a
  for j in range(len(t)-1):
    w[j+1]=w[j]+h*f(w[j],t[j])
  return w[:,0]

def p(w_a):
  return k(w_a)[len(t)-1]

init_velocity=o.newton(p,0) 

plt.subplot(211)
plt.plot(t,k(init_velocity),label='numerical_solution.')
plt.plot(t,50*t-5*t**2,'+',ms='8',label='accurate_solution.') 
plt.plot(t,k(40),'g',label='candidate solution.') 
for j in range(41,47):
  plt.plot(t,k(j),'g')
plt.xlabel('t.')
plt.ylabel('y.')
plt.ylim(bottom=0) 
plt.title('D²y=-g.')
plt.legend() 

#solution using numpy.argmin().
w_a_list=np.linspace(0,80,10000)
w_b_list=[] 
for j in w_a_list:
  w_b_list.append(p(j))
r=np.argmin(abs(np.array(w_b_list))) 
solution=k(w_a_list[r])

plt.subplot(212)
plt.plot(t,solution,label='solution using numpy.argmin().')
plt.xlabel('t.')
plt.ylabel('y.')
plt.ylim(bottom=0)
plt.legend()  
plt.show() 