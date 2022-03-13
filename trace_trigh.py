# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:01:01 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

x = np.arange(-2,2,0.001)
y1 = np.sinh(x)
y2 = np.cosh(x)

xmax=3
xmin=-xmax
ymax=3
ymin=-ymax

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$\sinh~x$')
plt.plot(x,y2, label='$\cosh~x$')

plt.axis([xmin, xmax, ymin, ymax], 'equal')
plt.grid()
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.savefig('trigh.png', dpi=200)
#plt.show()
plt.close()
