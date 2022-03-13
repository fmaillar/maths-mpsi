# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:35:27 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt


x = np.arange(-np.pi,np.pi,0.01)
x3 = np.arange(-2,2,0.001)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = 1./y3

y3[:-1][np.diff(y3) < 0] = np.nan
y4[:-1][np.diff(y4) > 0] = np.nan
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$\sin~x$')
plt.plot(x,y2, label='$\cos~x$')
plt.plot(x,y3, label='$\\textrm{tan}~x$')
plt.plot(x,y4, label='$\\textrm{cotan}~x$')
#Trace des asymptotes
#asymptotes
#tangente
plt.plot(-np.pi/2*x3/x3, x3 , ls = (0, (5, 10)), lw=0.5, color='green')
plt.plot(np.pi/2*x3/x3, x3 , ls = (0, (5, 10)), lw=0.5, color='green')
#cotangente
plt.plot(-np.pi*x3/x3 , x3, ls = (0, (5, 10)), lw=0.5, color='red')
plt.plot(np.pi*x3/x3 , x3, ls = (0, (5, 10)), lw=0.5, color='red')

plt.grid()
#plt.xlim(0,4)
plt.ylim(-2,2)
#plt.title('How to calculate the Natural logarithm in python ?',fontsize=10)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y$',fontsize=8)
plt.legend()
plt.savefig('trig.png', dpi=200)
#plt.show()
plt.close()
