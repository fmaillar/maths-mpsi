# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:18:04 2022

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

x = np.arange(1,5,0.001)
x1 = np.arange(0,5,0.001)

y1 = np.arccosh(x)
y2 = np.cosh(x1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$argcosh~x$')
plt.plot(x1,y2, label='$cosh~x$')
plt.plot(x1,x1, label='$x$')

plt.axis([0, 5, 0, 5], 'equal')
plt.grid()
plt.xlim(0,5)
plt.ylim(0,5)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.savefig('argcosh.png', dpi=200)
plt.show()
plt.close()