import numpy as np
import matplotlib.pyplot as plt 

t=[0]
h=10
x=[1]
  
def f(t,x):
  return 1/(t**2+x**2)
  
j=1 
while j>=1:
  k1=h*f(t[-1],x[-1])
  k2=h*f(t[-1]+h/2,x[-1]+k1/2)
  k3=h*f(t[-1]+h/2,x[-1]+k2/2)
  k4=h*f(t[-1]+h,x[-1]+h)
  t.append(j*h)
  x.append(x[-1]+(k1+2*k2+2*k3+k4)/6)
  if t[-1]==3.5e6:
    break
  else:
    True
  j=j+1

print('x(3.5×10^6)=',x[-1],'..')  

plt.plot(t,x)
plt.xlabel('t.')
plt.ylabel('x.')
plt.title('x behaviour in 0 to infinity domain.') 

plt.text(1e6,2,'x(3.5×10^6)= 2.9523643678871117..',fontsize=10) 
plt.text(1e6,1.8,'x converges for large t..',fontsize=10)
plt.show() 
  