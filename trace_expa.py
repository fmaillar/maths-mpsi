# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:18:54 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

def function(a,x):
    return np.exp(x*np.log(a))

x = np.arange(-4,4,0.01)

a1=2
a2=1./2
a3=1.5
y1 = function(a1,x)
y2 = function(a2,x)
y3 = function(a3,x)
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.plot(x,y1, label='$a=2>1$')
plt.plot(x,y2, label='$a=1/2<1$')
plt.plot(x,y3, label='$a=3/2>1$')
plt.grid()
plt.xlim(-3,3)
plt.ylim(0,4)
#plt.title('How to calculate the Natural logarithm in python ?',fontsize=10)
plt.xlabel('$x$',fontsize=8)
plt.ylabel('$y=exp_a(x)$',fontsize=8)
plt.legend()
plt.savefig('expa.png', dpi=200)
plt.close()
