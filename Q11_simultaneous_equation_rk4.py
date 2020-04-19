import numpy as np
import matplotlib.pyplot as plt 

t=np.linspace(0,1,100)
h=t[1]-t[0] 

u=np.zeros([len(t),3])
u[0]=[3,-1,1]

def f(t,u):
  du1=u[0]+2*u[1]-2*u[2]+np.exp(-t) 
  du2=u[1]+u[2]-2*np.exp(-t)
  du3=u[0]+2*u[1]+np.exp(-t)
  return np.array([du1,du2,du3])

for j in range(len(t)-1):
  k1=h*f(t[j],u[j])
  k2=h*f(t[j]+h/2,u[j]+k1/2)
  k3=h*f(t[j]+h/2,u[j]+k2/2)
  k4=h*f(t[j]+h,u[j]+k3) 
  u[j+1]=u[j]+(k1+2*k2+2*k3+k4)/6

plt.plot(t,u[:,0],label='u_1(t).')
plt.plot(t,u[:,1],label='u_2(t).')
plt.plot(t,u[:,2],label='u_3(t).')
plt.xlabel('t.')

plt.legend()
plt.show() 