# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np

def func(x):
    return np.sin(x)
N=500
x= np.linspace(0.0,10.0,N)
data=func(x)
y=data
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

#generate some noise
noise = np.random.uniform(-.5,.5,N)
plt.plot(x,noise)
plt.show()

#add noise to data
y=y+noise
plt.plot(x,y)
plt.show()

from scipy.ndimage import convolve
from scipy.ndimage import gaussian_filter

#smooth data with gaussian_filter
result = gaussian_filter(y, sigma=10)
plt.plot(x,data)
plt.plot(x,result)

plt.show()
