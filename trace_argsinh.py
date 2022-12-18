# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:10:51 2022

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

x = np.arange(-4,4,0.001)

y1 = np.arcsinh(x)
y2 = np.sinh(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$\\textrm{argsinh}~x$')
plt.plot(x,y2, label='$\\textrm{sinh}~x$')
plt.plot(x,x, label='$x$')

#plt.axis([-4, 4, -4, 4], 'equal')
plt.grid()
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.savefig('argsinh.png')
#plt.show()
plt.close()
