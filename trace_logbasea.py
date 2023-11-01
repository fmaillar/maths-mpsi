# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:02:21 2022

@author: e_fmaill
"""


import numpy as np
import matplotlib as mpl

mpl.rcParams["text.usetex"] = True
import matplotlib.pyplot as plt


def function(a, x):
    return np.log(x) / np.log(a)


plt.clf()
plt.close("all")

x = np.arange(0.01, 4, 0.01)
a1 = 2
a2 = 1.0 / 3
y1 = function(a1, x)
y2 = function(a2, x)
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color="k")
ax.axvline(x=0, color="k")
plt.plot(x, y1, label="$a>1$")
plt.plot(x, y2, label="$a<1$")
# plt.plot(x, (x-1)/np.log(a1), '--')
# plt.plot(x, (x-1)/np.log(a2), '--')
plt.grid()
plt.xlim(0, 4)
# plt.title('How to calculate the Natural logarithm in python ?',fontsize=10)
plt.xlabel("$x$", fontsize=8)
plt.ylabel("$y=ln_a(x)$", fontsize=8)
plt.legend()
plt.savefig("logbase.png", dpi=200)
# plt.show()
plt.close()
