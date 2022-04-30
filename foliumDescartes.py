# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:44:04 2022

@author: e_fmaill
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True


eps = 1e-1
a = -1
b = 100
N = int(10*(b-a))
A = 1
t1 = np.linspace(-b, a-eps, N)
t2 = np.linspace(a+eps, b, N)
x1 = A*t1/(1+t1**3)
y1 = t1*x1
x2 = A*t2/(1+t2**3)
y2 = t2*x2

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_aspect(1)
ax.set_xlim(-0.75, 0.75)
ax.set_ylim(-0.75, 0.75)

x = np.linspace(-1.5, 1.5)
y = -x - 1/3*A

ax.plot(x1, y1, x2, y2, color='orange')
ax.plot(x, y, '--', color='red')

ax.grid('True')
plt.savefig('folium.png')
plt.close(fig)
