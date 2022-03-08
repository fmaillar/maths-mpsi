# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:27:52 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt


x1 = np.arange(-1,1,0.001)
x2 = np.arange(0,np.pi,0.01)
x3 = np.arange(0.5,np.pi,0.01)

y1 = np.arccos(x1)
y2 = np.cos(x2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x1,y1, label='$\\textrm{arccos}~x$')
plt.plot(x2,y2, label='$\cos~x$')
plt.plot(x3,x3, label='$x$')

plt.axis([-2, 3.5, -2, 3.5], 'equal')
plt.grid()
plt.xlim(-2,3.5)
plt.ylim(-2,3.5)
#plt.title('How to calculate the Natural logarithm in python ?',fontsize=10)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
plt.savefig('arccos.png', dpi=200)
plt.show()
#plt.close()