How can I find the parameters of a function that fits properly with a given data?

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize, polyfit

n=50
x=np.linspace(0,10,n)
jitterAmp=4.
jitter=jitterAmp*(np.random.random(n)-0.5)
y=x+jitter

plt.plot(x,y,'o')
plt.show()

m,b=polyfit(x,y,1)
[m,b]

plt.plot(x,y,'o',hold=True)
t=np.array([0,10])
plt.plot(t,m*t+b)
plt.show()



Now we can make it more general:
1.Define data; i.e. x,y
2.Define curve; i.e. m*t+b
3.Get the parameters back from optimize.curve_fit:

def fitFunction(t,m,b):
    return(m*t+b)
p,cov=optimize.curve_fit(fitFunction,x,y)

p

As we can see the parameters are exactly the same as the best line fits in data.