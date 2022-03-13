# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:04:38 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

eps = 1./10000
x1 = np.arange(-2,-eps,0.001)
x2 = np.arange(eps,2, 0.001)
x = np.concatenate([x1, x2])
y1 = np.tanh(x)
y2 = 1./y1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$\\textrm{tanh}~x$')
plt.plot(x,y2, label='$\\textrm{cotanh}~x$')

plt.axis([-2, 2, -2, 2], 'equal')
plt.grid()
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.savefig('tanh.png', dpi=200)
#plt.show()
plt.close()
