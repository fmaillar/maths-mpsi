# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:27:27 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

def function(a,x):
    return x**a

x = np.arange(0.01,4,0.01)

a0=0
a1=2
a2=1
a3=0.5
a4=-2

y0 = function(a0,x)
y1 = function(a1,x)
y2 = function(a2,x)
y3 = function(a3,x)
y4 = function(a4,x)

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y0, label='$a=0$')
plt.plot(x,y1, label='$a>1$')
plt.plot(x,y2, label='$a=1$')
plt.plot(x,y3, label='$0<a<1$')
plt.plot(x,y4, label='$a<0$')
plt.grid()
plt.xlim(0,4)
plt.ylim(0,4)
#plt.title('How to calculate the Natural logarithm in python ?',fontsize=10)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y=a^x$',fontsize=8)
plt.legend()
plt.savefig('puiss.png', dpi=200)
#plt.show()
plt.close()
