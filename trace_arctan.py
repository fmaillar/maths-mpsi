# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:33:34 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl

mpl.rcParams["text.usetex"] = True
import matplotlib.pyplot as plt


x1 = np.arange(-4, 4, 0.001)
x2 = np.arange(-np.pi / 2, np.pi / 2, 0.001)
x3 = np.arange(-4, 4, 0.001)


y1 = np.arctan(x1)
y2 = np.tan(x2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect("equal", adjustable="box")
ax.axhline(y=0, color="k")
ax.axvline(x=0, color="k")
plt.plot(x1, y1, label="$\\textrm{arctan}~x$")
plt.plot(x2, y2, label="$tan~x$")
plt.plot(x3, x3, label="$x$")
# asymptotes
plt.plot(x3, np.pi / 2 * x3 / x3, "r", ls=(0, (5, 10)), lw=0.5, label="$x,y=\pm\pi/2$")
plt.plot(x3, -np.pi / 2 * x3 / x3, "r", ls=(0, (5, 10)), lw=0.5)
plt.plot(np.pi / 2 * x3 / x3, x3, "r", ls=(0, (5, 10)), lw=0.5)
plt.plot(-np.pi / 2 * x3 / x3, x3, "r", ls=(0, (5, 10)), lw=0.5)

plt.grid()
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.xlabel("$x$", fontsize=8)
plt.ylabel("$y$", fontsize=8)
plt.legend()
ax.axhline(y=0, color="k")
ax.axvline(x=0, color="k")
plt.savefig("arctan.png")
# plt.show()
plt.close()
