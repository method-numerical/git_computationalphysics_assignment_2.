import numpy as np
import matplotlib.pyplot as plt

h=0.1
n=int(1/h+1)

t=np.linspace(1,2,n)
y=t/(1+np.log(t)) 
w=np.ones(len(t))

def f(y,t):
  return y/t-(y/t)**2

for j in range(len(t)-1):
  w[j+1]=w[j]+h*f(w[j],t[j])

a=w-y; r=a/y 
print('absolute errors=',a) 
print('relative errors=',r) 

plt.plot(w,'+',label='approximate_solution.')
plt.plot(y,label='exact_solution.')
plt.plot(a,'+',label='absolute_errors.')
plt.plot(r,label='relative_errors.')
plt.xlabel('t')
plt.legend()
plt.show() 