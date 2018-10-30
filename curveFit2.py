import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, polyfit

n=10
x=np.linspace(-10,10,n)
jitterAmp=5
jitter=jitterAmp*(np.random.random(n))*220

y=7*x*x*x+5*x*x+7*x+2+jitter
z=7*x*x*x+5*x*x+7*x+2
plt.plot(x,y,'o')
plt.plot(x,z,'-')
plt.show()

def fitFunction(t,m,b,c):
    return(m*t*t*t+b*t*t+c*t+2)
p,cov=optimize.curve_fit(fitFunction,x,y)
p

t=np.array([0,10])
plt.plot(x,fitFunction(x,p[0],p[1],p[2]))
plt.plot(x,z,'o')
plt.show()