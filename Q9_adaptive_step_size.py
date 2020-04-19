import numpy as np
import matplotlib.pyplot as plt

t=[1];w=[-2];
h=1;del0=1e-4;

def f(t,y):
  return (y+y**2)/t

def g(h,t,w):
  k1=h*f(t,w)
  k2=h*f(t+h/2,w+k1/2)
  k3=h*f(t+h/2,w+k2/2)
  k4=h*f(t+h,w+k3)
  return w+(k1+2*k2+2*k3+k4)/6
  
i=0
while i>=0:
  y_1=g(2*h,t[-1],w[-1])
  y_2=g(h,t[-1],w[-1])
  ratio=del0/abs(y_2-y_1)
  h_new=h*ratio**0.2
  if abs(y_2-y_1)<=del0:
    t.append(t[-1]+h)
    w.append(y_2)
    h=h_new
  else:
    h=h_new
  if t[-1]>3:
    del(t[-1]);del(w[-1]);
    break
  i=i+1

print('number of mesh points=',len(t)) 
print('mesh points=',t)
print('solution at mesh points=',w,'..') 
plt.plot(t,w,label='Dy=(y+y²)/t.')
plt.xlabel('t.')
plt.ylabel('y.')
plt.legend();plt.show()


