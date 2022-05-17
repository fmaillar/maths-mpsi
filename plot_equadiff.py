# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:47:58 2022.

@author: e_fmaill
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# import math

mpl.rcParams['text.usetex'] = True


x = np.linspace(-5, 5, 40)
y = x
a = -0.25
C1 = 1
C2 = 2
y2 = C1*np.exp(a*x)
y3 = C2*np.exp(a*x)

X, Y = np.meshgrid(x, y)

u = 1
v = a*Y

fig, ax = plt.subplots(figsize=(7, 7))
ax.quiver(X, Y, u, v, headaxislength=1, headlength=1, width=0.001)
ax.plot(x, y2)
ax.plot(x, y3)
ax.scatter(0, C1, color='red', label=f'$C={C1}$')
ax.scatter(0, C2, color='blue', label=f'$C={C2}$')
# ax.xaxis.set_ticks([])
# ax.yaxis.set_ticks([])
ax.axis([-5, 5, 0, 4])
ax.set_aspect('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.title("Deux solutions de $y'=ay, a=-1/4$")
plt.tight_layout()
# ax.Axes
# plt.show()
plt.savefig('Equa-diff', dpi=200)
