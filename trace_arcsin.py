# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:43:31 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

eps = 1.0/100
x = np.arange(-np.pi/2+eps,np.pi/2-eps,0.01)
x2 = np.arange(-1.3,1.3,0.01)
y1 = np.sin(x)
y2 = np.arcsin(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$\sin~x$')
plt.plot(x,y2, label='$\\textrm{arcsin}~x$')
plt.plot(x2,x2, label='$x$')

plt.axis([-2, 2, -2, 2], 'equal')
plt.grid()
plt.xlim(-2,2)
plt.ylim(-2,2)
#plt.title('How to calculate the Natural logarithm in python ?',fontsize=10)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
plt.savefig('arcsin.png', dpi=200)
#plt.show()
plt.close()
