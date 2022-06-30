# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:14:35 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

def function(x):
    return np.log(x)

x = np.arange(0.01,4,0.01)

y = function(x)
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y, label='$\ln~x$')
plt.plot(x,x-1, label='$x-1$')
plt.grid()
plt.xlim(0,4)
#plt.title('How to calculate the Natural logarithm in python ?',fontsize=10)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()

plt.savefig('lognep.png', dpi=200)
plt.show()
plt.close()