# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:24:21 2022

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

x = np.arange(-2,2,0.001)

y1 = np.arctanh(x)
y2 = np.tanh(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$\\textrm{argtanh}~x$')
plt.plot(x,y2, label='$\\textrm{tanh}~x$')
plt.plot(x,x, label='$x$')
#asymptotes
plt.plot(x, x/x,'r', ls = (0, (5, 10)), lw=0.5, label='$x,y=\pm 1$')
plt.plot(x, -x/x, 'r', ls = (0, (5, 10)), lw=0.5)
plt.plot(x/x, x, 'r', ls = (0, (5, 10)), lw=0.5)
plt.plot(-x/x, x, 'r', ls = (0, (5, 10)), lw=0.5)


plt.axis([-2, 2, -2, 2], 'equal')
plt.grid()
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.savefig('argtanh.png', dpi=200)
#plt.show()
plt.close()
