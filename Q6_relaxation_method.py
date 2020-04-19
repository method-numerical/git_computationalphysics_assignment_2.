import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10,70);h=t[1]-t[0]


w=np.zeros(len(t))

v=np.zeros([7,len(t)])

k=np.zeros(len(t))

i=0
while i>=0:
  for j in range(len(t)):
    k[j]=w[j] 
  for j in range(1,len(t)-1):
    w[j]=(w[j-1]+w[j+1]+10*h**2)/2
  if np.max(abs(k-w))<0.01:
    break
  elif (39<i<1001)and(i%100==0):
    v[int(i/100)-4]=w
  else:
    True
  i=i+1

plt.plot(t,w,'g',label='numerical_solution.') 
for j in range(7):
  plt.plot(t,v[j],'y',label='candidate_solution.')
plt.plot(t,50*t-5*t**2,'+',label='true_solution.')
plt.xlabel('t.')
plt.ylabel('y.')
plt.legend()
plt.show()
